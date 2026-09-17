import random


class Sudoku:

    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        empty = self.find_empty()

        if empty is None:
            return True

        row, col = empty

        numbers = list(range(1, 10))
        random.shuffle(numbers)

        for num in numbers:
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

        return None

    @classmethod
    def generate(cls, difficulty="medium"):
        difficulty_map = {
            "easy": 30,
            "medium": 40,
            "hard": 50
        }

        if difficulty not in difficulty_map:
            raise ValueError(
                "Difficulty must be easy, medium, or hard."
            )

        cells_to_remove = difficulty_map[difficulty]

        # Start with an empty board
        board = [[0 for _ in range(9)] for _ in range(9)]

        # Generate a random complete solution
        sudoku = cls(board)
        sudoku.solve()

        # Keep a copy of the complete solution
        solution = [row[:] for row in sudoku.board]

        # Remove numbers to create the puzzle
        positions = [
            (row, col)
            for row in range(9)
            for col in range(9)
        ]

        random.shuffle(positions)

        for row, col in positions[:cells_to_remove]:
            sudoku.board[row][col] = 0

        return sudoku.board, solution