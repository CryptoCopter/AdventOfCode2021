#!/usr/bin/env python3

from typing import Tuple, Dict
from math import ceil


def load_input(path: str) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    subs: Dict[str, Tuple[str, str]] = {}

    with open(path, "r") as f:
        start = f.readline().strip()
        f.readline()
        for line in f:
            parts = line.strip().split(" -> ")
            subs[parts[0]] = (parts[0][0] + parts[1], parts[1] + parts[0][1])

    return start, subs


def cyber_pcr(start: str, subs: Dict[str, Tuple[str, str]], steps: int) -> int:
    patterns: Dict[str, int] = {}
    for pattern in subs:
        occurrences = start.count(pattern)
        if occurrences:
            patterns[pattern] = occurrences

    for _ in range(steps):
        new_patterns = {}
        for pattern in patterns:
            subl, subr = subs[pattern]
            new_patterns[subl] = new_patterns.get(subl, 0) + patterns[pattern]
            new_patterns[subr] = new_patterns.get(subr, 0) + patterns[pattern]

        patterns = new_patterns

    monomers: Dict[str, int] = {}
    for pattern in patterns:
        monomers[pattern[0]] = monomers.get(pattern[0], 0) + patterns[pattern]
        monomers[pattern[1]] = monomers.get(pattern[1], 0) + patterns[pattern]

    occurrences = [ceil(x / 2) for x in monomers.values()]
    return max(occurrences) - min(occurrences)


if __name__ == "__main__":
    start, subs = load_input("input.txt")

    # part 1
    print(cyber_pcr(start, subs, 10))

    # part 2
    print(cyber_pcr(start, subs, 40))
