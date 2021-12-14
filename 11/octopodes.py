#!/usr/bin/env python3

from typing import List, Tuple


neighbours = [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1)]


def load_input(path: str) -> List[List[int]]:
    octopodes: List[List[int]] = []
    with open(path, "r") as f:
        for line in f:
            octopodes.append([int(x) for x in line.strip()])
    return octopodes


def is_valid(j, k) -> bool:
    return 0 <= j <= 9 and 0 <= k <= 9


def flash(
    octopus: Tuple[int, int], octopodes: List[List[int]], flashed: List[List[bool]]
) -> int:
    flashing: List[Tuple[int, int]] = [octopus]
    flashed[octopus[0]][octopus[1]] = True
    flashes = 0

    while flashing:
        j, k = flashing.pop()
        flashes += 1

        for neighbour in neighbours:
            x = j + neighbour[0]
            y = k + neighbour[1]
            if is_valid(x, y):
                if not flashed[x][y]:
                    octopodes[x][y] += 1
                    if octopodes[x][y] > 9:
                        flashing.append((x, y))
                        flashed[x][y] = True

    return flashes


def blitzdings(octopodes: List[List[int]], steps: int) -> None:
    flashes = 0
    for step in range(steps):
        # phase 1
        for row in octopodes:
            row[:] = [x + 1 for x in row]

        # phase 2
        flashed: List[List[bool]] = [[False for _ in range(10)] for _ in range(10)]
        round_flashes = 0
        for j in range(10):
            for k in range(10):
                if octopodes[j][k] > 9 and not flashed[j][k]:
                    round_flashes += flash((j, k), octopodes, flashed)
        flashes += round_flashes

        if round_flashes == 100:
            print(f"Synchronisation in step {step + 1}")
            return

        # phase 3
        for row in octopodes:
            row[:] = [x if x <= 9 else 0 for x in row]

        if step == 99:
            print(f"Flashes after 100 steps: {flashes}")

    return


if __name__ == "__main__":
    octopodes = load_input("input.txt")
    blitzdings(octopodes, 10000)
