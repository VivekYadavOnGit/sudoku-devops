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