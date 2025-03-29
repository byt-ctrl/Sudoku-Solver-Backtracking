# WRITTEN BY OM [byt-ctrl]
# 9*9 SOLDUKU SOLVER

import tkinter as tk  # Import the GUI's tkinter
from tkinter import messagebox  # To display error messages

class SudokuSolver :
    def __init__(self) :

        """Create the Sudoku grid and solve button after initializing the window."""

        self.window=tk.Tk()  # Make a window
        self.window.title("Sudoku Solver")  # Change the window's title
        self.cells=[[None for _ in range(9)] for _ in range(9)]  # Construct a 9x9 entry widget grid.
        self.build_grid()  # To generate the grid, use the method.
        self.add_solve_button()  # Create the solve button using the call method
        self.window.mainloop()  # Launch the GUI event loop.

    def build_grid(self) :

        """makes the Sudoku board's input grid."""
        for row in range(9) :  # Repeat for every row.
            for col in range(9):  # Repeat for every coloum.
               # Make an Entry widget for every grid cell.
                cell=tk.Entry(self.window,width=3,font=("Arial",18),justify="center",bd=0,relief="solid")
                
                # To make 3x3 blocks stand out more , add padding.
                top_padding=15 if row%3==0 else 0
                left_padding=15 if col%3==0 else 0
                bottom_padding=2 if row==8 else 1
                right_padding=2 if col==8 else 1
                
                # Insert the grid's Entry widget.
                cell.grid(row=row,column=col,ipadx=5,ipady=10,sticky="nsew",padx=(left_padding,right_padding),pady=(top_padding,bottom_padding))
                self.cells[row][col]=cell  # Save the Entry widget to be accessed later.



    def add_solve_button(self) :

        """The 'Solve' button is created."""
        solve_button=tk.Button(self.window,text="Solve 9x9 Sudoku",font=("Arial",22),command=self.solve_puzzle)
        solve_button.grid(row=9,column=0,columnspan=9,pady=12)  # Position the button at the grid's bottom.



    def solve_puzzle(self) :
        """takes care of the Sudoku problem solution."""
        
        puzzle=self.extract_input_board()  # Use user input to retrieve the Sudoku board.
        if puzzle is None :  # Stop's solving if there was an input mistake.
            return
        if self.solve_using_backtracking(puzzle) :  # If the board can be solved
            self.update_board_display(puzzle)  # Add the solution to the grid.
        else:
            messagebox.showinfo("Error" , "No solution exists.")  # Display an error message if it cannot be resolved.



    def extract_input_board(self) :
        """takes user input and extracts the Sudoku board."""

        puzzle=[]
        try:
            for row in range(9) :
                row_values=[]
                for col in range(9) :
                    value=self.cells[row][col].get()  # Use the Entry widget to retrieve the value.
                    if value=="" :
                        row_values.append(0)  # Assign 0 to empty cells.
                    elif value.isdigit() and 1 <= int(value) <= 9 :
                        row_values.append(int(value))  # Include real numbers
                    else :
                        raise ValueError("Invalid input! Enter numbers between 1 and 9.")  # Identify incorrect input
                puzzle.append(row_values)
            return puzzle
        except ValueError as e :
            messagebox.showinfo("Error",str(e))  # Display an error message if the input is incorrect.
            return None



    def update_board_display(self, puzzle) :

        """Updates the solved Sudoku board to the grid."""
        for row in range(9) :
            for col in range(9) :
                self.cells[row][col].delete(0,tk.END)  # Empty the current cell.
                self.cells[row][col].insert(0,str(puzzle[row][col]))  # Enter the value that has been solved.

    def placement_of_numbers(self,puzzle,row,col,number,row_sets,col_sets,block_sets) :

        """determines if a number may be entered into the specified cell."""
        block_index=(row // 3) * 3 + (col // 3)  # Locate the block
        if number in row_sets[row] or number in col_sets[col] or number in block_sets[block_index] :
            return False  # If the number is already present in the block, column, or row, return False.
        return True

# MAIN LOGIC 

    def solve_using_backtracking(self, puzzle) :

        """use backtracking to solve the Sudoku problem."""
        # Make sets to keep track of the numbers in every block, row, and column (for quicker lookup).
        row_sets=[set() for _ in range(9)]
        col_sets=[set() for _ in range(9)]
        block_sets=[set() for _ in range(9)]
        
        # Add the puzzle's starting values to the sets.
        for row in range(9) :
            for col in range(9):
                number=puzzle[row][col]
                if number!=0:
                    row_sets[row].add(number)
                    col_sets[col].add(number)
                    block_sets[(row // 3) * 3 + (col // 3)].add(number)

        def backtrack():

            """utility for recursive backtracking."""
            for row in range(9):
                for col in range(9):
                    if puzzle[row][col] == 0:  # Finding the empty cell
                        for number in range(1,10):  # Try the digits 1 through 9.
                            if self.placement_of_numbers(puzzle,row,col,number,row_sets,col_sets,block_sets) :

                                # If the number is valid, enter it.
                                puzzle[row][col]=number
                                row_sets[row].add(number)
                                col_sets[col].add(number)
                                block_sets[(row // 3) * 3 + (col // 3)].add(number)

                                if backtrack():  # To solve the following cell, repeat.
                                    return True

                                # If no valid number was discovered , go back.
                                puzzle[row][col] = 0
                                row_sets[row].remove(number)
                                col_sets[col].remove(number)
                                block_sets[(row // 3) * 3 + (col // 3)].remove(number)
                        return False  # If this cell's valid number is not discovered
            return True  # If the entire board is solved, return True.

        return backtrack()  # Launch the algorithm for backtracking

# To launch the application, create an instance of the SudokuSolver class.
SudokuSolver()

# END
