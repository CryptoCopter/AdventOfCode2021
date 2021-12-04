#!/usr/bin/env python3

from typing import List


def load_input(path: str) -> List[int]:
    depths: List[int] = []

    with open(path, "r") as f:
        for line in f:
            depths.append(int(line))

    return depths


def count_increasing_depths(depths: List[int]) -> int:
    increases = 0
    depth = depths[0]

    for next in depths[1:]:
        if next > depth:
            increases += 1
        depth = next

    return increases


def compute_windows(depths: List[int]) -> List[int]:
    return [x + y + z for x, y, z in zip(depths[:-2], depths[1:-1], depths[2:])]


if __name__ == "__main__":
    depths = load_input("input.txt")
    print(f"Number of depth measurements: {len(depths)}")
    increases = count_increasing_depths(depths)
    print(f"Number of depth increases: {increases}")
    windows = compute_windows(depths)
    window_increases = count_increasing_depths(windows)
    print(f"Number of depth increases /w sliding window: {window_increases}")
