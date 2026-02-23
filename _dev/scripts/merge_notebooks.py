#!/usr/bin/env python
"""Merge two notebooks: Part 1 header + base cells + Part 2 header + extension cells."""
import argparse
import copy
import nbformat


def merge(title, part1_label, part2_label, base, extension, output):
    nb1 = nbformat.read(base, as_version=4)
    nb2 = nbformat.read(extension, as_version=4)

    merged = nbformat.v4.new_notebook()
    merged.metadata = copy.deepcopy(nb1.metadata)

    merged.cells = (
        [nbformat.v4.new_markdown_cell(source=f"# {title}\n\n## {part1_label}")]
        + copy.deepcopy(nb1.cells)
        + [nbformat.v4.new_markdown_cell(source=f"## {part2_label}")]
        + copy.deepcopy(nb2.cells)
    )

    nbformat.validate(merged)
    nbformat.write(merged, output)
    print(f"  {output}  ({len(nb1.cells)} + {len(nb2.cells)} cells)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("base")
    p.add_argument("extension")
    p.add_argument("output")
    p.add_argument("--title", default="LazyDINO Tutorial")
    p.add_argument("--part1-label", default="Part 1")
    p.add_argument("--part2-label", default="Part 2")
    a = p.parse_args()
    merge(a.title, a.part1_label, a.part2_label, a.base, a.extension, a.output)
