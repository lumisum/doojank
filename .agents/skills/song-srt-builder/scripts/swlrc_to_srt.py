#!/usr/bin/env python3
"""Convert Xingyu SWLRC line timings plus trusted lyrics to line-level SRT."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path


TIMESTAMP = r"\d{2,}:[0-5]\d\.\d{3}"
TIME_RE = re.compile(r"^(?P<minutes>\d{2,}):(?P<seconds>[0-5]\d)\.(?P<millis>\d{3})$")
LINE_RE = re.compile(rf"^\[({TIMESTAMP}),({TIMESTAMP})\]$")
TOKEN_RE = re.compile(rf"^<({TIMESTAMP}),({TIMESTAMP})>(?P<text>.*)$")


@dataclass
class TimedLine:
    start_ms: int
    end_ms: int
    tokens: list[tuple[int, int, str]] = field(default_factory=list)


def time_to_ms(value: str) -> int:
    match = TIME_RE.fullmatch(value)
    if not match:
        raise ValueError(f"Invalid timestamp: {value!r}")
    minutes = int(match.group("minutes"))
    seconds = int(match.group("seconds"))
    millis = int(match.group("millis"))
    return (minutes * 60 + seconds) * 1000 + millis


def parse_swlrc(path: Path) -> list[TimedLine]:
    lines: list[TimedLine] = []
    current: TimedLine | None = None

    try:
        raw_lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise ValueError(f"Cannot read SWLRC file: {exc}") from exc

    for number, raw in enumerate(raw_lines, start=1):
        line = raw.strip()
        if not line:
            continue

        line_match = LINE_RE.fullmatch(line)
        if line_match:
            if current is not None:
                lines.append(current)
            current = TimedLine(
                start_ms=time_to_ms(line_match.group(1)),
                end_ms=time_to_ms(line_match.group(2)),
            )
            continue

        token_match = TOKEN_RE.fullmatch(line)
        if token_match:
            if current is None:
                raise ValueError(f"SWLRC token appears before a line header at line {number}.")
            current.tokens.append(
                (
                    time_to_ms(token_match.group(1)),
                    time_to_ms(token_match.group(2)),
                    token_match.group("text"),
                )
            )
            continue

        # SWLRC metadata is bracketed but is not a timed line.
        if line.startswith("[") and line.endswith("]"):
            continue
        raise ValueError(f"Unrecognized SWLRC content at line {number}: {raw!r}")

    if current is not None:
        lines.append(current)
    return lines


def normalized_letters(text: str) -> str:
    """Ignore spacing and punctuation while retaining letters and numbers."""
    normalized: list[str] = []
    for char in unicodedata.normalize("NFKC", text):
        if unicodedata.category(char)[:1] in {"L", "N"}:
            normalized.append(char.casefold())
    return "".join(normalized)


def load_lyrics(path: Path) -> list[str]:
    try:
        raw = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ValueError(f"Cannot read lyrics file: {exc}") from exc
    # Empty lines are structural only; retain each non-empty line verbatim.
    return [line.strip() for line in raw.splitlines() if line.strip()]


def format_srt_time(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"


def build_srt(lyrics: list[str], timed_lines: list[TimedLine]) -> tuple[str, list[str]]:
    if len(lyrics) != len(timed_lines):
        raise ValueError(
            f"Line count mismatch: {len(lyrics)} non-empty lyric lines, "
            f"but {len(timed_lines)} timed SWLRC blocks. Check skipped lines or headers."
        )

    warnings: list[str] = []
    cues: list[str] = []
    previous_start = -1
    previous_end = -1

    for index, (lyric, timed) in enumerate(zip(lyrics, timed_lines), start=1):
        if timed.start_ms < 0 or timed.end_ms <= timed.start_ms:
            raise ValueError(f"Invalid interval for lyric line {index}: {timed.start_ms}–{timed.end_ms} ms.")
        if not timed.tokens:
            raise ValueError(f"SWLRC line {index} has no aligned tokens.")
        if timed.start_ms < previous_start:
            raise ValueError(f"SWLRC timestamps move backward at lyric line {index}.")

        token_text = "".join(token for _, _, token in timed.tokens)
        expected = normalized_letters(lyric)
        actual = normalized_letters(token_text)
        if expected != actual:
            raise ValueError(
                f"Text mismatch at lyric line {index}: source {lyric!r}; "
                f"aligned tokens {token_text!r}. Correct the input or review alignment first."
            )

        previous_token_start = timed.start_ms
        for token_start, token_end, _ in timed.tokens:
            if token_start < timed.start_ms or token_end > timed.end_ms or token_end <= token_start:
                raise ValueError(f"Invalid token interval within lyric line {index}.")
            if token_start < previous_token_start:
                raise ValueError(f"Token timestamps move backward within lyric line {index}.")
            previous_token_start = token_start

        if timed.start_ms < previous_end:
            overlap = previous_end - timed.start_ms
            warnings.append(f"Cues {index - 1} and {index} overlap by {overlap} ms; timings were preserved.")

        cues.append(
            f"{index}\n{format_srt_time(timed.start_ms)} --> {format_srt_time(timed.end_ms)}\n{lyric}\n"
        )
        previous_start = timed.start_ms
        previous_end = timed.end_ms

    return "\n".join(cues), warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lyrics", required=True, type=Path, help="Trusted plain-text lyrics, one lyric line per line.")
    parser.add_argument("--swlrc", required=True, type=Path, help="Aligned Xingyu SWLRC file.")
    parser.add_argument("--output", required=True, type=Path, help="Destination SRT path.")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing SRT file.")
    args = parser.parse_args()

    try:
        lyrics = load_lyrics(args.lyrics)
        if not lyrics:
            raise ValueError("The lyrics file contains no non-empty lyric lines.")
        timed_lines = parse_swlrc(args.swlrc)
        srt_text, warnings = build_srt(lyrics, timed_lines)
        if args.output.exists() and not args.overwrite:
            raise ValueError(f"Output already exists: {args.output}. Choose another path or pass --overwrite.")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(srt_text, encoding="utf-8", newline="\n")
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
