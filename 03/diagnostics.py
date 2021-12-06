#!/usr/bin/env python3

from typing import List, Tuple


def load_input(path: str) -> List[List[int]]:
    report: List[List[int]] = []
    with open(path, "r") as f:
        for line in f:
            report.append([int(x) for x in line.strip()])
    return report


def most_common(report: List[List[int]], index: int) -> Tuple[int, int]:
    column = [row[index] for row in report]
    zeros = column.count(0)
    ones = column.count(1)
    if zeros > ones:
        return 0, 1
    else:
        return 1, 0


def compute_rates(report: List[List[int]]) -> int:
    gamma = 0
    epsilon = 0

    for i in range(len(report[0])):
        most, least = most_common(report, i)
        gamma = (gamma << 1) | most
        epsilon = (epsilon << 1) | least

    return gamma * epsilon


def binay_to_decimal(number: List[int]) -> int:
    n = 0
    for digit in number:
        n = (n << 1) | digit
    return n


def life_support(report: List[List[int]]) -> int:
    oxygen = report
    co2 = report[:]
    for i in range(len(report[0])):
        if len(oxygen) == len(co2) == 1:
            break
        if len(oxygen) > 1:
            most, least = most_common(oxygen, i)
            oxygen = [row for row in oxygen if row[i] == most]
        if len(co2) > 1:
            most, least = most_common(co2, i)
            co2 = [row for row in co2 if row[i] == least]

    oxygen_rating = binay_to_decimal(oxygen[0])
    co2_rating = binay_to_decimal(co2[0])
    return oxygen_rating * co2_rating


if __name__ == "__main__":
    report = load_input("input.txt")

    # Part 1
    rates = compute_rates(report)
    print(rates)

    # Part 2
    life_support_rating = life_support(report)
    print(life_support_rating)
