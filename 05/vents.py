#!/usr/bin/env python3

from typing import List, Tuple, Dict


def load_input(path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    vents: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
    with open(path, "r") as f:
        for line in f:
            coords = line.split(" -> ")
            start = coords[0].split(",")
            stop = coords[1].strip().split(",")
            vents.append(((int(start[0]), int(start[1])), (int(stop[0]), int(stop[1]))))

    return vents


def coordinates_to_lines(
    vents: List[Tuple[Tuple[int, int], Tuple[int, int]]]
) -> List[Tuple[int, int]]:
    lines: List[Tuple[int, int]] = []

    for vent in vents:
        start = vent[0]
        x_diff = vent[1][0] - vent[0][0]
        y_diff = vent[1][1] - vent[0][1]
        steps = max(abs(x_diff), abs(y_diff))
        x_step = int(x_diff / steps)
        y_step = int(y_diff / steps)

        for i in range(steps + 1):
            lines.append((start[0] + (x_step * i), start[1] + (y_step * i)))

    return lines


def find_intersections(lines: List[Tuple[int, int]]) -> int:
    overlaps = 0

    points: Dict[Tuple[int, int]] = {}
    for point in lines:
        occurences = points.get(point, 0) + 1
        points[point] = occurences

    for point in points:
        if points[point] > 1:
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    vents = load_input("input.txt")

    # part 1
    straight_vents = [x for x in vents if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    straight_lines = coordinates_to_lines(straight_vents)
    intersections = find_intersections(straight_lines)
    print(intersections)

    # part 2
    lines = coordinates_to_lines(vents)
    intersections = find_intersections(lines)
    print(intersections)
