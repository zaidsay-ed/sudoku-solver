import tkinter as tk
from tkinter import messagebox 

class SudokuGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[ 0 for i in range(9)] for i in range(9)]
        self.cells = [[ None for i in range(9)] for i in range(9)]
        self.create.board()
        self.create_buttons()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(frame, width =3, font = ('Arial', 14), borderwidth=1, relief = "solid", justify = "center")
                cell.grid(row = row, column = col, padx = 2, pady = 2)

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady = 10)
        solve_button = tk.Button(frame, text="Solve", command=self.solve)
        solve_button.pack(side=tk.LEFT, padx=5)
        clear_button = tk.Button(frame, text="Clear", command=self.clear)
        clear_button.pack(side=tk.LEFT, padx=5)

    def get_board(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[row][col].get()
                self.board[row][col] = int(value) if value.isdigit() else 0
