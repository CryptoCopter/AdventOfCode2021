#!/usr/bin/env python3

from typing import List, Tuple


def load_input(path: str) -> List[List[int]]:
    grid: List[List[int]] = []
    with open(path, "r") as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    return grid


def this_is_definitely_the_low_point(grid: List[List[int]]) -> List[Tuple[int, int]]:
    low_points: List[Tuple[int, int]] = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i > 0 and grid[i - 1][j] <= grid[i][j]:
                continue
            if j > 0 and grid[i][j - 1] <= grid[i][j]:
                continue
            if i < (len(grid) - 1) and grid[i + 1][j] <= grid[i][j]:
                continue
            if j < (len(grid[i]) - 1) and grid[i][j + 1] <= grid[i][j]:
                continue
            low_points.append((i, j))

    return low_points


def compute_danger(grid: List[List[int]], low_points: List[Tuple[int, int]]) -> int:
    return sum([grid[i][j] + 1 for i, j in low_points])


def basins(grid: List[List[int]], low_points: List[Tuple[int, int]]) -> int:
    considered: List[List[bool]] = [
        [False for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    basin_sizes: List[int] = []
    for low_point in low_points:
        basin_size = 0
        considering: List[Tuple[int, int]] = [low_point]
        considered[low_point[0]][low_point[1]] = True
        while considering:
            i, j = considering.pop()
            basin_size += 1
            if i > 0 and not considered[i - 1][j] and grid[i - 1][j] < 9:
                considering.append((i - 1, j))
                considered[i - 1][j] = True
            if j > 0 and not considered[i][j - 1] and grid[i][j - 1] < 9:
                considering.append((i, j - 1))
                considered[i][j - 1] = True
            if i < (len(grid) - 1) and not considered[i + 1][j] and grid[i + 1][j] < 9:
                considering.append((i + 1, j))
                considered[i + 1][j] = True
            if (
                j < (len(grid[i]) - 1)
                and not considered[i][j + 1]
                and grid[i][j + 1] < 9
            ):
                considering.append((i, j + 1))
                considered[i][j + 1] = True
        basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    grid = load_input("input.txt")
    low_points = this_is_definitely_the_low_point(grid)

    # Part 1
    danger = compute_danger(grid, low_points)
    print(danger)

    # Part 2
    basin_size = basins(grid, low_points)
    print(basin_size)
