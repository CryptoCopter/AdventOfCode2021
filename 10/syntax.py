#!/usr/bin/env python3

from typing import List, Tuple


POINTS_CORRUPTED = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


POINTS_COMPLETED = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def load_input(path: str) -> List[str]:
    chunks: List[str] = []
    with open(path, "r") as f:
        for line in f:
            chunks.append(line.strip())
    return chunks


def lets_do_both_at_once_i_guess(chunks: List[str]) -> Tuple[int, int]:
    score_corrupted = 0
    scores_incomplete: List[int] = []

    for line in chunks:
        pairs: List[str] = []
        for char in line:
            if char in PAIRS:
                pairs.append(PAIRS[char])
            else:
                if char != pairs.pop():
                    score_corrupted += POINTS_CORRUPTED[char]
                    pairs = []
                    break
        if pairs:
            score = 0
            pairs.reverse()
            for char in pairs:
                score *= 5
                score += POINTS_COMPLETED[char]
            scores_incomplete.append(score)

    scores_incomplete.sort()

    return score_corrupted, scores_incomplete[int(len(scores_incomplete) / 2)]


if __name__ == "__main__":
    chunks = load_input("input.txt")

    # Part 1 & 2
    part1, part2 = lets_do_both_at_once_i_guess(chunks)
    print(part1)
    print(part2)
