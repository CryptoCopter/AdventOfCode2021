#!/usr/bin/env python3

from typing import List


def load_input(path: str) -> List[int]:
    with open(path, "r") as f:
        return [int(x) for x in f.readline().strip().split(",")]


def do_the_crabwalk(crab_people: List[int]) -> int:
    fuel_req = [0] * (max(crab_people) + 1)

    for mr_crabs in crab_people:
        for i in range(len(fuel_req)):
            fuel_req[i] += abs(mr_crabs - i)

    return min(fuel_req)


def crab_engineering(crab_people: List[int]) -> int:
    fuel_req = [0] * (max(crab_people) + 1)

    for mr_crabs in crab_people:
        for i in range(len(fuel_req)):
            steps = abs(mr_crabs - i)
            fuel_req[i] += int((steps * (steps + 1)) / 2)

    return min(fuel_req)


if __name__ == "__main__":
    crab_people = load_input("input.txt")

    # Part 1
    min_fuel = do_the_crabwalk(crab_people)
    print(min_fuel)

    # Part 2
    weird_fuel = crab_engineering(crab_people)
    print(weird_fuel)
