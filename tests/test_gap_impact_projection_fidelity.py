"""Authored gap impact values must survive human projection.

ADR-Kit 0.12.0 rendered authoring-1.6 scalar impacts as empty ``**Impact:** <br>``
lines. This check binds each canonical gap to its generated projection.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
LOGICAL_DIR = REPO_ROOT / "adrs" / "logical"
PROJECTION_DIR = REPO_ROOT / "adrs" / "adr-projection" / "logical"
HEADING = re.compile(r"^### (GAP-\d+):[ \t]*(.*)$", re.MULTILINE)
IMPACT = re.compile(r"^\*\*Impact:\*\*[ \t]*(.*?)\s*$", re.MULTILINE)
BLOCKING = re.compile(r"^\*\*Blocking:\*\*[ \t]*(Yes|No)\s*$", re.MULTILINE)


def _normalize(text: str) -> str:
    return " ".join(text.split())


def _sections(text: str) -> dict[str, str]:
    matches = list(HEADING.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        gap_id = match.group(1)
        if gap_id in sections:
            raise AssertionError(f"duplicate projection heading {gap_id}")
        sections[gap_id] = text[match.start() : end]
    return sections


def test_authored_gap_impacts_render_exactly() -> None:
    projected: dict[str, tuple[Path, str]] = {}
    for path in sorted(PROJECTION_DIR.glob("*.md")):
        for gap_id, section in _sections(path.read_text(encoding="utf-8")).items():
            if gap_id in projected:
                raise AssertionError(f"{gap_id} appears in more than one projection")
            projected[gap_id] = (path, section)

    authored = 0
    for source in sorted(LOGICAL_DIR.glob("*.yaml")):
        document = yaml.safe_load(source.read_text(encoding="utf-8"))
        for gap in document.get("gaps") or []:
            authored += 1
            gap_id = gap["id"]
            impact = gap["impact"]
            assert isinstance(impact, str) and impact, f"{gap_id} has no authored impact"
            assert gap_id in projected, f"{gap_id} has no projection"
            path, section = projected[gap_id]
            heading = HEADING.search(section)
            assert heading is not None
            assert _normalize(heading.group(2)) == _normalize(str(gap["question"]))
            impact_match = IMPACT.search(section)
            assert impact_match is not None, f"{gap_id} impact line missing in {path.name}"
            rendered = impact_match.group(1).replace("<br>", "").strip()
            assert rendered == impact, (
                f"{gap_id} rendered {rendered!r} != authored {impact!r} in {path.name}"
            )
            assert impact_match.group(1) != "<br>"
            blocking = BLOCKING.search(section)
            assert blocking is not None, f"{gap_id} blocking line missing"
            expected = "Yes" if gap["blocking"] else "No"
            assert blocking.group(1) == expected

    assert authored == 43
    assert len(projected) == authored
