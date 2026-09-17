from flask import Blueprint, jsonify, render_template, request, session

from .sudoku import Sudoku


main = Blueprint("main", __name__)


@main.route("/")
def home():
    # Generate a new Sudoku puzzle.
    puzzle, solution = Sudoku.generate("medium")

    # Store the current game in the session.
    session["puzzle"] = puzzle
    session["solution"] = solution
    session["mistakes"] = 0

    return render_template("index.html", board=puzzle)


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

    # Get the solution for the current game.
    solution = session.get("solution")

    if solution is None:
        return jsonify({
            "valid": False,
            "message": "No active game."
        }), 400

    # Compare user's board with the actual solution.
    if board == solution:
        return jsonify({
            "valid": True,
            "message": "Congratulations! 🎉 Correct solution."
        })

    return jsonify({
        "valid": False,
        "message": "Incorrect solution."
    })


@main.route("/move", methods=["POST"])
def check_move():
    data = request.get_json()

    if not data:
        return jsonify({
            "correct": False,
            "message": "Invalid request."
        }), 400

    required_fields = ["row", "col", "number"]

    if any(field not in data for field in required_fields):
        return jsonify({
            "correct": False,
            "message": "Missing move information."
        }), 400

    row = data["row"]
    col = data["col"]
    number = data["number"]

    if not all(
        isinstance(value, int)
        for value in [row, col, number]
    ):
        return jsonify({
            "correct": False,
            "message": "Move values must be integers."
        }), 400

    if not (0 <= row < 9 and 0 <= col < 9):
        return jsonify({
            "correct": False,
            "message": "Invalid cell position."
        }), 400

    if not (1 <= number <= 9):
        return jsonify({
            "correct": False,
            "message": "Number must be between 1 and 9."
        }), 400

    solution = session.get("solution")
    puzzle = session.get("puzzle")

    if solution is None or puzzle is None:
        return jsonify({
            "correct": False,
            "message": "No active game."
        }), 400

    # Prevent changing an original puzzle cell.
    if puzzle[row][col] != 0:
        return jsonify({
            "correct": False,
            "message": "This cell cannot be changed."
        }), 400

    if solution[row][col] == number:
        return jsonify({
            "correct": True,
            "mistakes": session.get("mistakes", 0),
            "message": "Correct move! ✅"
        })

    # Incorrect move.
    mistakes = session.get("mistakes", 0) + 1
    session["mistakes"] = mistakes

    return jsonify({
        "correct": False,
        "mistakes": mistakes,
        "message": "Incorrect move. ❌"
    })