#!/usr/bin/env pypy3

from typing import List, Dict


class Cave:
    def __init__(self, name: str, is_large: bool, neighbours: List):
        self.name = name
        self.is_large = is_large
        self.neighbours = neighbours

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self) -> str:
        return f"{self.name} -> {[x.name for x in self.neighbours]}"

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return self.name.__hash__()


def load_input(path: str) -> List[Cave]:
    caves: Dict[str, Cave] = {}
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split("-")
            if parts[0] in caves:
                left = caves[parts[0]]
            else:
                left = Cave(name=parts[0], is_large=parts[0].isupper(), neighbours=[])
                caves[parts[0]] = left

            if parts[1] in caves:
                right = caves[parts[1]]
            else:
                right = Cave(name=parts[1], is_large=parts[1].isupper(), neighbours=[])
                caves[parts[1]] = right

            left.neighbours.append(right)
            right.neighbours.append(left)

    return list(caves.values())


def visit_tiny_cave(path: List[Cave], cave: Cave) -> bool:
    if cave.name == "start":
        return False

    caves: Dict[Cave, int] = {}
    for cave in path:
        if not cave.is_large:
            visits = caves.get(cave, 0) + 1
            if visits > 1:
                return False
            caves[cave] = visits
    return True


def backtrack(cave: Cave, path: List[Cave], second_edition: bool) -> List[List[Cave]]:
    path_from_here = path[:]
    path_from_here.append(cave)
    paths_from_here: List[List[Cave]] = []
    for neighbour in cave.neighbours:
        if neighbour in path and not neighbour.is_large:
            if not second_edition or not visit_tiny_cave(path_from_here, neighbour):
                continue

        if neighbour.name == "end":
            finished_path = path_from_here[:]
            finished_path.append(neighbour)
            paths_from_here.append(finished_path)
            continue

        paths_from_neighbour: List[List[Cave]] = backtrack(
            cave=neighbour, path=path_from_here, second_edition=second_edition
        )
        if paths_from_neighbour:
            paths_from_here += paths_from_neighbour

    return paths_from_here


def pathfinder_1st_edition(caves: List[Cave]) -> int:
    start = [x for x in caves if x.name == "start"][0]

    paths = backtrack(cave=start, path=[], second_edition=False)

    return len(paths)


def pathfinder_2nd_edition(caves: List[Cave]) -> int:
    start = [x for x in caves if x.name == "start"][0]

    paths = backtrack(cave=start, path=[], second_edition=True)

    return len(paths)


if __name__ == "__main__":
    caves = load_input("input.txt")

    # Part 1
    paths = pathfinder_1st_edition(caves)
    print(paths)

    # Part 2
    paths = pathfinder_2nd_edition(caves)
    print(paths)
