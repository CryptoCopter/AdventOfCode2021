#!/usr/bin/env python3

from typing import List, Tuple, Dict


digit_map = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
distinct = [1, 4, 7]  # checking for 8 does not help us in any way...


def load_input(path: str) -> List[Tuple[List[str], List[str]]]:
    displays: List[Tuple[List[str], List[str]]] = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            patterns = parts[0].strip().split(" ")
            output = parts[1].strip().split(" ")
            sorted_output = ["".join(sorted(x)) for x in output]
            displays.append((patterns, sorted_output))

    return displays


def find_simple(displays: List[Tuple[List[str], List[str]]]) -> int:
    count = 0
    for display in displays:
        count += len(
            [
                x
                for x in display[1]
                if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7
            ]
        )

    return count


def get_signals_of_length(signals: List[str], length: int) -> List[str]:
    return [x for x in signals if len(x) == length]


def filter_letters(lookup: Dict[str, str], pattern: str, locations: str) -> None:
    for letter in locations:
        lookup[letter] = "".join(set(lookup[letter]) & set(pattern))


def discard_letters(lookup: Dict[str, str], pattern: str, locations: str) -> None:
    for letter in locations:
        lookup[letter] = "".join(set(lookup[letter]) - set(pattern))


def invert_pattern(pattern: str) -> str:
    inverted = "abcdefg"
    return "".join(set(inverted) - set(pattern))


def find_letters_by_occurrences(patterns: List[str], n: int) -> str:
    concat = "".join(patterns)
    return "".join([x for x in set(concat) if concat.count(x) == n])


def create_reverse_map(lookup: Dict[str, str]) -> Dict[str, str]:
    reverse_map: Dict[str, str] = {}

    for digit in range(10):
        sections = ""
        for letter in digit_map[digit]:
            sections = f"{sections}{lookup[letter]}"
        reverse_map["".join(sorted(sections))] = str(digit)

    return reverse_map


def decode_display(output: List[str], reverse_map: Dict[str, str]) -> int:
    digit_str = "".join([reverse_map[x] for x in output])
    return int(digit_str)


def decode_bullshit(displays: List[Tuple[List[str], List[str]]]) -> int:
    display_sum = 0
    for display in displays:
        signals: List[str] = display[0]
        lookup = {
            "a": "abcdefg",
            "b": "abcdefg",
            "c": "abcdefg",
            "d": "abcdefg",
            "e": "abcdefg",
            "f": "abcdefg",
            "g": "abcdefg",
        }

        # step 1: filter uniques
        for digit in distinct:
            pattern = get_signals_of_length(
                signals, len(digit_map[digit])
            )  # should only ever get 0 or 1 result
            if pattern:
                filter_letters(
                    lookup, pattern[0], digit_map[digit]
                )  # keep the mapping in the matching locations
                discard_letters(lookup, pattern[0], invert_pattern(digit_map[digit]))

        # step 2: so something with 2/3/5
        patterns = get_signals_of_length(signals, 5)
        if patterns:
            # section e is only present once (2-digit), b once (5-digit), c twice (2&3), f twice (3&5)
            single_occurrence = find_letters_by_occurrences(
                patterns, 1
            )  # one of these is e, the other is b
            filter_letters(lookup, single_occurrence, "eb")
            discard_letters(lookup, single_occurrence, invert_pattern("eb"))

            # turns out, all of this does nothing...
            # dual_occurrence = find_letters_by_occurrences(patterns, 2)  # one of these is c, the other is f
            # keep(mapping, dual_occurrence, "cf")
            # discard(mapping, dual_occurrence, invert_pattern("cf"))

        # step 3 do something with 0/6/9
        patterns = get_signals_of_length(signals, 6)
        # sections c, d, e only occur twice each
        if patterns:
            dual_occurrence = find_letters_by_occurrences(patterns, 2)
            filter_letters(lookup, dual_occurrence, "cde")
            discard_letters(lookup, dual_occurrence, invert_pattern("cde"))

        for key in lookup:
            assert len(lookup[key]) == 1

        reverse_map = create_reverse_map(lookup)
        displayed_number = decode_display(display[1], reverse_map)
        display_sum += displayed_number

    return display_sum


if __name__ == "__main__":
    garbled = load_input("input.txt")

    # Part 1
    simple_digits = find_simple(garbled)
    print(simple_digits)

    # part 2
    all_digits = decode_bullshit(garbled)
    print(all_digits)
