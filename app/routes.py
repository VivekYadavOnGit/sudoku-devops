from flask import Blueprint, jsonify, render_template, request

from .sudoku import Sudoku

main = Blueprint("main", __name__)


INITIAL_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


@main.route("/")
def home():
    return render_template("index.html", board=INITIAL_BOARD)


@main.route("/check", methods=["POST"])
def check_solution():
    data = request.get_json()

    if not data or "board" not in data:
        return jsonify({
            "valid": False,
            "message": "Invalid request."
        }), 400

    board = data["board"]

    if len(board) != 9 or any(len(row) != 9 for row in board):
        return jsonify({
            "valid": False,
            "message": "Board must be 9x9."
        }), 400

    sudoku = Sudoku(board)

    if sudoku.find_empty() is not None:
        return jsonify({
            "valid": False,
            "message": "The puzzle is not complete."
        })

    # Create a copy of the original puzzle.
    solution = [row[:] for row in INITIAL_BOARD]

    # Solve the original puzzle.
    solver = Sudoku(solution)

    if not solver.solve():
        return jsonify({
            "valid": False,
            "message": "Unable to solve puzzle."
        }), 500

    # Compare user's board with the actual solution.
    if board == solver.board:
        return jsonify({
            "valid": True,
            "message": "Congratulations! 🎉 Correct solution."
        })

    return jsonify({
        "valid": False,
        "message": "Incorrect solution."
    })