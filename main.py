#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The front page is the entry.png beside this file, drawn in this
repository's session. The program copies it to /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    source = HERE / "entry.png"
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.png"
    shutil.copyfile(source, target)
    if _sha256(source) != _sha256(target):
        raise RuntimeError(
            f"output verification failed: {target} does not match {source}"
        )


if __name__ == "__main__":
    main()
