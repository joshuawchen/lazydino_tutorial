#!/usr/bin/env python
"""Merge two READMEs: title + Part 1 + Part 2."""
import argparse
from pathlib import Path


def merge(title, part1_label, part2_label, base, extension, output):
    txt1 = Path(base).read_text().strip()
    txt2 = Path(extension).read_text().strip()

    combined = (
        f"# {title}\n\n"
        f"# {part1_label}\n\n"
        f"{txt1}\n\n"
        f"---\n\n"
        f"# {part2_label}\n\n"
        f"{txt2}\n"
    )

    Path(output).write_text(combined)
    print(f"  {output}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("base")
    p.add_argument("extension")
    p.add_argument("output")
    p.add_argument("--title", default="LazyDINO Tutorial Readme")
    p.add_argument("--part1-label", default="Part 1")
    p.add_argument("--part2-label", default="Part 2")
    a = p.parse_args()
    merge(a.title, a.part1_label, a.part2_label, a.base, a.extension, a.output)
