"""Check PNG files referenced by the active city and Coroa builder, without Godot's cache."""
from __future__ import annotations

import re
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "maps/sucateia/sucateia.tscn", ROOT / "scripts/world/coroa_district.gd"]
PATTERN = re.compile(r"res://([^\"'\s)]+\.png)")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def inspect(path: Path) -> tuple[int, int, int]:
    with path.open("rb") as stream:
        if stream.read(8) != PNG_SIGNATURE:
            raise ValueError("bad PNG signature")
        width = height = 0
        chunks = 0
        saw_end = False
        while not saw_end:
            header = stream.read(8)
            if len(header) != 8:
                raise ValueError("truncated chunk header")
            length, kind = struct.unpack(">I4s", header)
            data = stream.read(length)
            checksum = stream.read(4)
            if len(data) != length or len(checksum) != 4:
                raise ValueError(f"truncated {kind!r} chunk")
            expected = struct.unpack(">I", checksum)[0]
            actual = zlib.crc32(kind + data) & 0xFFFFFFFF
            if actual != expected:
                raise ValueError(f"CRC mismatch in {kind!r}")
            if kind == b"IHDR":
                width, height = struct.unpack(">II", data[:8])
                if not width or not height:
                    raise ValueError("empty image")
            chunks += 1
            saw_end = kind == b"IEND"
    return width, height, chunks


def main() -> int:
    refs = {match.group(1) for file in FILES for match in PATTERN.finditer(file.read_text(encoding="utf-8"))}
    errors = []
    checked_bytes = 0
    for relative in sorted(refs):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"MISSING {relative}")
            continue
        checked_bytes += path.stat().st_size
        try:
            width, height, chunks = inspect(path)
            print(f"OK {relative} {width}x{height} chunks={chunks}")
        except (OSError, ValueError) as exc:
            errors.append(f"BAD {relative}: {exc}")
    print(f"COROA_SOURCE_PNGS checked={len(refs)-len(errors)} bytes={checked_bytes} errors={len(errors)}")
    for error in errors:
        print(error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
