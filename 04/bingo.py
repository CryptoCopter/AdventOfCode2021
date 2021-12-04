#!/usr/bin/env python3

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class BingoBoard:
    board: List[List[Tuple[int, bool]]]

    def transpose(self) -> List[List[Tuple[int, bool]]]:
        return list(map(list, zip(*self.board)))

    @staticmethod
    def _check_win(board: List[List[Tuple[int, bool]]]) -> bool:
        for row in board:
            done = all([x[1] for x in row])
            if done:
                return True
        return False

    def check_win(self) -> bool:
        return self._check_win(self.board) or self._check_win(self.transpose())

    def play(self, number: int) -> bool:
        for row in self.board:
            try:
                index = row.index((number, False))
                row[index] = (number, True)
                return True
            except ValueError:
                continue

        return False

    def calculate_score(self, called_number: int) -> int:
        sum_unchecked = 0
        for row in self.board:
            sum_unchecked += sum([x[0] for x in row if not x[1]])
        return sum_unchecked * called_number

    def play_game(self, numbers: List[int]) -> Tuple[int, int]:
        turn = 0

        for number in numbers:
            change = self.play(number)
            turn += 1
            if change and self.check_win():
                score = self.calculate_score(number)
                return turn, score

        return -1, 0


def load_input(path: str) -> Tuple[List[int], List[BingoBoard]]:
    boards: List[BingoBoard] = []
    with open(path, "r") as f:
        numbers = [int(x) for x in f.readline().strip().split(",")]
        f.readline()

        board: List[List[Tuple[int, bool]]] = []
        for line in f:
            if line == "\n":
                boards.append(BingoBoard(board))
                board = []
                continue
            board.append(
                [(int(x), False) for x in line.replace("  ", " ").strip().split(" ")]
            )

        boards.append(BingoBoard(board))

    return numbers, boards


def find_winning_score(scores: List[Tuple[int, int]]) -> int:
    turns = [x[0] for x in scores]
    winning_turn = min(turns)
    index = turns.index(winning_turn)
    return scores[index][1]


def find_losing_score(scores: List[Tuple[int, int]]) -> int:
    turns = [x[0] for x in scores]
    winning_turn = max(turns)
    index = turns.index(winning_turn)
    return scores[index][1]


if __name__ == "__main__":
    numbers, boards = load_input("input.txt")
    print(numbers)
    print(boards)

    scores = [board.play_game(numbers) for board in boards]
    print(find_winning_score(scores))
    print(find_losing_score(scores))
