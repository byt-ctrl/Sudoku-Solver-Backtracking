# 🧩 Sudoku Solver Application
The **Sudoku Solver** is a graphical user interface (GUI) application built with Python's **Tkinter** library. It enables users to input a 9x9 Sudoku puzzle and solves it using the **backtracking algorithm**. The program is designed to be intuitive and user-friendly, allowing users to easily enter a puzzle and find the solution with the click of a button.

---
### 🛠️ How It Works

The application provides a window displaying a 9x9 grid, where each cell can be filled with numbers between 1 and 9. The user can input their Sudoku puzzle directly into the grid. After entering the puzzle, the user clicks the **"Solve 9x9 Sudoku"** button to solve the puzzle .

#### Upon clicking the solve button:

1.  The program extracts the input from the grid.
    
2.  It checks for any invalid entries (non-numeric values or numbers outside the 1-9 range).
    
3.  If the input is valid, the program uses the **backtracking algorithm** to find a solution.
    
4.  If a solution is found, it is displayed in the grid. If no solution exists, an error message is shown.
    
---
### 🔄 Backtracking Algorithm

The core of this Sudoku solver is the **backtracking algorithm**, which works by recursively trying to fill the empty cells of the grid with numbers 1 through 9. The algorithm ensures that the following conditions are met:

1.  **Row**: The number must not already be present in the same row.
    
2.  **Column**: The number must not already be present in the same column.
    
3.  **Block**: The number must not already be present in the 3x3 block.
    

The algorithm proceeds as follows:

1.  It finds an empty cell (denoted by 0) and tries placing numbers 1 through 9 in that cell.
    
2.  For each number, it checks if placing it violates the Sudoku rules. If the number is valid, it proceeds to the next empty cell.
    
3.  If no valid number can be placed in a cell, it "backtracks," undoing the last placement and trying the next possible number.
    

This process continues until the entire grid is filled, or it is determined that no solution exists.

---
### ⚙️ Key Features

-   **User-friendly Interface**: The GUI allows for easy input and visualization of the puzzle.
    
-   **Input Validation**: Ensures users can only enter valid numbers (1-9) or leave cells empty.
    
-   **Backtracking Solver**: Uses a recursive backtracking algorithm to find the solution.
    
-   **Error Handling**: Displays error messages if the input is invalid or if the puzzle has no solution.
    

### 📝 Example Usage

1.  Open the application, and a 9x9 grid will appear with empty cells.
    
2.  Enter numbers from 1 to 9 in the grid (use 0 for empty cells).
    
3.  Press the **"Solve 9x9 Sudoku"** button to solve the puzzle.
    
4.  If the puzzle is solvable, the solution will be displayed. If not, an error message will appear.
    
---
### 🚀 Conclusion

This **Sudoku Solver** demonstrates how the **backtracking algorithm** can efficiently solve Sudoku puzzles. With its user-friendly interface and robust error handling, this application provides a simple yet effective way to solve Sudoku puzzles of any difficulty.

---
## 🤝 Contributing :

If u have any idea's feel free to contribute   
Fork the repository if needed , make your changes, and submit a pull request.


## 📜 License:

This project is licensed under the **Apache 2.0 License**.

---
