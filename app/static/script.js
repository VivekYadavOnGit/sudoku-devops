const checkButton = document.getElementById("check-button");
const message = document.getElementById("message");


function getBoard() {
    const inputs = document.querySelectorAll(".sudoku-board input");

    const board = [];

    for (let row = 0; row < 9; row++) {
        const currentRow = [];

        for (let col = 0; col < 9; col++) {
            const value = inputs[row * 9 + col].value;

            currentRow.push(value === "" ? 0 : Number(value));
        }

        board.push(currentRow);
    }

    return board;
}


// Validate a player's move.
async function validateMove(input) {
    const number = Number(input.value);

    // Ignore empty input.
    if (input.value === "") {
        message.textContent = "";
        return;
    }

    const row = Number(input.dataset.row);
    const col = Number(input.dataset.col);

    const response = await fetch("/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            row: row,
            col: col,
            number: number
        })
    });

    const result = await response.json();

    message.textContent = result.message;
}


// Listen for player input.
const inputs = document.querySelectorAll(".sudoku-board input");

inputs.forEach((input) => {
    if (!input.readOnly) {
        input.addEventListener("input", () => {
            validateMove(input);
        });
    }
});


// Check the complete solution.
checkButton.addEventListener("click", async () => {
    const board = getBoard();

    const response = await fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            board: board
        })
    });

    const result = await response.json();

    message.textContent = result.message;
});