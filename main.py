"""Write one office-life joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun "Make the AI Judge Laugh"
(u-rama-melon-make-the-ai-judge-laugh-302d0825): a single line about
office life, under 200 characters. Pure Python standard library.
"""

import os
from pathlib import Path

ENTRY = "The thermostat is set to a temperature nobody likes, which is the closest thing this office has to consensus."
# 109 characters, within the 1-200 gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
