#!/usr/bin/env python3

from typing import List, Tuple, Set


def load_input(path: str) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    dots: List[Tuple[int, int]] = []
    folds: List[Tuple[int, int]] = []
    with open(path, "r") as f:
        for line in f:
            if line == "\n":
                break
            x, y = line.strip().split(",")
            dots.append((int(x), int(y)))
        for line in f:
            direction, line = line.strip().split(" ")[2].split("=")
            if direction == "x":
                index = 0
            else:
                index = 1
            folds.append((index, int(line)))

    return dots, folds


def the_spice_is_vital_to_space_travel_the_spacing_guild_and_its_navigators_who_the_spice_has_mutated_over_4000_years_use_the_orange_spice_gas_which_gives_them_the_ability_to_fold_space(
    dots: List[Tuple[int, int]], fold: Tuple[int, int]
) -> List[Tuple[int, int]]:
    direction, line = fold
    new_dots: Set[Tuple[int, int]] = set()
    for dot in dots:
        if dot[direction] < line:
            new_dots.add(dot)
        else:
            new_coord = line + (line - dot[direction])
            if direction == 0:
                new_dots.add((new_coord, dot[1]))
            else:
                new_dots.add((dot[0], new_coord))

    return list(new_dots)


def print_dots(dots: List[Tuple[int, int]]) -> None:
    min_x = min(dot[0] for dot in dots)
    max_x = max(dot[0] for dot in dots)
    min_y = min(dot[1] for dot in dots)
    max_y = max(dot[1] for dot in dots)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    dots, folds = load_input("input.txt")

    # part 1
    dots = the_spice_is_vital_to_space_travel_the_spacing_guild_and_its_navigators_who_the_spice_has_mutated_over_4000_years_use_the_orange_spice_gas_which_gives_them_the_ability_to_fold_space(
        dots, folds[0]
    )
    print(len(dots))

    # part 2
    for fold in folds[1:]:
        dots = the_spice_is_vital_to_space_travel_the_spacing_guild_and_its_navigators_who_the_spice_has_mutated_over_4000_years_use_the_orange_spice_gas_which_gives_them_the_ability_to_fold_space(
            dots, fold
        )

    print_dots(dots)
