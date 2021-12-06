#!/usr/bin/env python3

from typing import List, Tuple


def load_input(path: str) -> List[int]:
    with open(path, "r") as f:
        return [int(x) for x in f.readline().strip().split(",")]


def pop_growth(start_pop: List[int], days: int) -> int:
    age_buckets: List[int] = [0] * 9
    for fish in start_pop:
        age_buckets[fish] += 1

    while days:
        next_pop = [0] * 9
        next_pop[6] = age_buckets[0]
        next_pop[8] = age_buckets[0]
        for i in range(8):
            next_pop[i] += age_buckets[i + 1]

        age_buckets = next_pop
        days -= 1

    return sum(age_buckets)


if __name__ == "__main__":
    starting_fish = load_input("input.txt")

    # part 1
    descendants = pop_growth(starting_fish, 80)
    print(descendants)

    # part 2
    descendants = pop_growth(starting_fish, 256)
    print(descendants)
