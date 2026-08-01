#!/usr/bin/env python3
"""Validate the request-to-code skill without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_SKILL_NAME = "request-to-code"
TOP_LEVEL_FIELD_PATTERN = re.compile(r"^([A-Za-z0-9_-]+):(?:[ \t]*(.*))?$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKILL_PATH_PATTERN = re.compile(r"`((?:references|scripts|assets)/[^`\s]+)`")
ALLOWED_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
PHASE_HEADING_PATTERN = re.compile(r"## Phase ([1-6]) [-—] .+")
REQUIRED_GATE_MARKERS = [
    "Pause at the end of Phases 1 and 2, and Phase 4 when it applies.",
    "Approve this diagnosis so I can create the plan? (yes/no)",
    "Do not implement until the user approves.",
    "End with one question naming only the requested delivery actions.",
]
REQUIRED_REQUEST_MARKERS = [
    "A direct chat request is sufficient. A ticket is optional.",
    "Local changes are the default delivery outcome.",
    "Do not infer commit, push, or PR creation from a ticket",
]
REQUIRED_COMMUNICATION_MARKERS = [
    "## User-facing communication",
    "Use plain, everyday language and short sentences.",
    "Keep routine reports to five bullets or fewer.",
    "Ask one clear question at a time.",
    "Do not paste raw logs, full patches, or checklist transcripts unless the user asks",
]


def decode_scalar(raw_value: str, field: str, errors: list[str]) -> str:
    """Decode the small inline-scalar subset used by required frontmatter fields."""
    value = raw_value.strip()
    if not value:
        return ""
    if value.startswith('"'):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError as exc:
            errors.append(f"frontmatter field {field!r} has invalid quoting: {exc.msg}")
            return ""
        if not isinstance(decoded, str):
            errors.append(f"frontmatter field {field!r} must be a string")
            return ""
        return decoded
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            errors.append(f"frontmatter field {field!r} has invalid quoting")
            return ""
        return value[1:-1].replace("''", "'")
    if value.endswith(('"', "'")):
        errors.append(f"frontmatter field {field!r} has invalid quoting")
        return ""
    return value


def parse_skill(skill_file: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    """Return top-level frontmatter fields and body text from SKILL.md."""
    try:
        text = skill_file.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read {skill_file}: {exc}")
        return {}, ""

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append("SKILL.md must start with a YAML frontmatter delimiter")
        return {}, ""

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        errors.append("SKILL.md frontmatter is missing its closing delimiter")
        return {}, ""

    fields: dict[str, str] = {}
    current_field: str | None = None
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if "\t" in line:
            errors.append(f"SKILL.md:{line_number}: tabs are not valid frontmatter indentation")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace():
            if current_field not in {"metadata"}:
                errors.append(f"SKILL.md:{line_number}: unexpected indented frontmatter content")
            continue
        match = TOP_LEVEL_FIELD_PATTERN.fullmatch(line)
        if not match:
            errors.append(f"SKILL.md:{line_number}: invalid top-level frontmatter syntax")
            current_field = None
            continue
        key, raw_value = match.group(1), match.group(2) or ""
        if key in fields:
            errors.append(f"SKILL.md:{line_number}: duplicate frontmatter field {key!r}")
        if key not in ALLOWED_FIELDS:
            errors.append(f"SKILL.md:{line_number}: unsupported frontmatter field {key!r}")
        fields[key] = raw_value
        current_field = key

    decoded_fields: dict[str, str] = {}
    for field, raw_value in fields.items():
        if field == "metadata" and not raw_value.strip():
            decoded_fields[field] = ""
        else:
            decoded_fields[field] = decode_scalar(raw_value, field, errors)
    for field in ("name", "description"):
        if field not in fields:
            errors.append(f"missing required frontmatter field {field!r}")
            decoded_fields[field] = ""

    body = "\n".join(lines[closing_index + 1 :]).strip()
    if not body:
        errors.append("SKILL.md body must not be empty")
    return decoded_fields, body


def content_outside_fences(body: str) -> str:
    """Remove fenced examples so structural checks inspect executable instructions only."""
    output: list[str] = []
    inside_fence = False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            inside_fence = not inside_fence
            continue
        if not inside_fence:
            output.append(line)
    return "\n".join(output)


def validate_structure(root: Path, fields: dict[str, str], body: str, errors: list[str]) -> None:
    """Validate metadata limits and the six-phase approval workflow."""
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not NAME_PATTERN.fullmatch(name):
        errors.append("name must use lowercase letters, numbers, and single hyphens")
    if len(name) > 64:
        errors.append("name must not exceed 64 characters")
    if name and name != EXPECTED_SKILL_NAME:
        errors.append(f"name must be {EXPECTED_SKILL_NAME!r}; found {name!r}")
    if not description:
        errors.append("description must not be empty")
    if len(description) > 1024:
        errors.append("description must not exceed 1024 characters")

    structural_body = content_outside_fences(body)
    phase_numbers = [
        int(match.group(1))
        for line in structural_body.splitlines()
        if (match := PHASE_HEADING_PATTERN.fullmatch(line.strip()))
    ]
    if phase_numbers != [1, 2, 3, 4, 5, 6]:
        errors.append(f"expected phases 1-6 as headings in order; found {phase_numbers!r}")
    for marker in REQUIRED_GATE_MARKERS:
        if marker not in structural_body:
            errors.append(f"missing approval-gate marker: {marker}")
    for marker in REQUIRED_REQUEST_MARKERS:
        if marker not in structural_body:
            errors.append(f"missing request-source marker: {marker}")
    for marker in REQUIRED_COMMUNICATION_MARKERS:
        if marker not in structural_body:
            errors.append(f"missing user-communication marker: {marker}")


def local_reference_targets(source: Path, text: str, root: Path) -> set[Path]:
    """Collect local Markdown links and skill-root resource paths."""
    targets: set[Path] = set()
    for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
        target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
        if not target or target.startswith(("#", "/")) or "://" in target:
            continue
        target = target.split("#", 1)[0]
        if target and not any(character in target for character in "*?[]"):
            targets.add((source.parent / target).resolve())
    for target in SKILL_PATH_PATTERN.findall(text):
        if not any(character in target for character in "*?[]"):
            targets.add((root / target.rstrip(".,;:")).resolve())
    return targets


def validate_references(root: Path, errors: list[str]) -> None:
    """Ensure local files referenced by skill Markdown exist inside the repository."""
    markdown_files = [root / "SKILL.md", root / "README.md"]
    markdown_files.extend(sorted((root / "references").glob("*.md")))
    for source in markdown_files:
        if not source.is_file():
            continue
        text = source.read_text(encoding="utf-8")
        for target in local_reference_targets(source, text, root):
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{source.relative_to(root)} references a path outside the skill: {target}")
                continue
            if not target.is_file():
                errors.append(
                    f"{source.relative_to(root)} references missing file {target.relative_to(root)}"
                )


def validate(root: Path) -> list[str]:
    """Run every skill validation and return human-readable errors."""
    errors: list[str] = []
    if not root.is_dir():
        return [f"skill path is not a directory: {root}"]
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return [f"SKILL.md not found under {root}"]

    fields, body = parse_skill(skill_file, errors)
    validate_structure(root, fields, body, errors)
    validate_references(root, errors)
    return errors


def main() -> int:
    """Validate the requested skill directory and return a shell-friendly status."""
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = validate(root)
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Skill validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
