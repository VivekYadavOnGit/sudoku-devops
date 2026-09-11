import pytest

from app import create_app
from app.sudoku import Sudoku


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def get_puzzle():
    return [
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


def get_solution():
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]


def test_valid_move():
    sudoku = Sudoku(get_puzzle())

    assert sudoku.is_valid(0, 2, 4) is True


def test_invalid_row_move():
    sudoku = Sudoku(get_puzzle())

    assert sudoku.is_valid(0, 2, 5) is False


def test_invalid_column_move():
    sudoku = Sudoku(get_puzzle())

    assert sudoku.is_valid(2, 0, 6) is False


def test_solve():
    sudoku = Sudoku(get_puzzle())

    assert sudoku.solve() is True
    assert sudoku.find_empty() is None


def test_incomplete_solution(client):
    response = client.post(
        "/check",
        json={"board": get_puzzle()}
    )

    assert response.status_code == 200
    assert response.json["valid"] is False
    assert response.json["message"] == "The puzzle is not complete."


def test_correct_solution(client):
    response = client.post(
        "/check",
        json={"board": get_solution()}
    )

    assert response.status_code == 200
    assert response.json["valid"] is True


def test_incorrect_solution(client):
    board = get_solution()

    # Change one value to create an incorrect solution.
    board[0][0] = 4

    response = client.post(
        "/check",
        json={"board": board}
    )

    assert response.status_code == 200
    assert response.json["valid"] is False


def test_invalid_board(client):
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    response = client.post(
        "/check",
        json={"board": board}
    )

    assert response.status_code == 400
    assert response.json["valid"] is False