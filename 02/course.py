#!/usr/bin/env python3

from typing import List, Tuple


def load_input(path: str) -> List[Tuple[int, int]]:
    course: List[Tuple[int, int]] = []
    with open(path, "r") as f:
        for line in f:
            parts = line.split(" ")
            value = int(parts[1])

            if parts[0] == "forward":
                course.append((value, 0))
            elif parts[0] == "down":
                course.append((0, value))
            else:
                course.append((0, -value))

    return course


def find_destination(course: List[Tuple[int, int]]) -> int:
    xdest = sum([x for x, _ in course])
    ydest = sum([y for _, y in course])
    return xdest * ydest


def aim_for_the_moon_or_something(course: List[Tuple[int, int]]) -> int:
    aim = 0
    xpos = 0
    ypos = 0

    for forward, turn in course:
        xpos += forward
        ypos += forward * aim
        aim += turn

    return xpos * ypos


if __name__ == "__main__":
    course = load_input("input.txt")
    print(course)
    destination = find_destination(course)
    print(destination)
    real_destination = aim_for_the_moon_or_something(course)
    print(real_destination)
