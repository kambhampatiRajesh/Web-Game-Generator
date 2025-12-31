import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        master.resizable(False, False) # Make window non-resizable

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Player status label
        self.status_label = tk.Label(self.master, text=f"Player {self.current_player}'s turn", font=('Arial', 16, 'bold'))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Game board buttons
        for r in range(3):
            for c in range(3):
                button = tk.Button(self.master, text="", font=('Arial', 30, 'bold'),
                                   width=4, height=2,
                                   command=lambda row=r, col=c: self.button_click(row, col))
                button.grid(row=r+1, column=c, padx=5, pady=5) # Offset by 1 for status label
                self.buttons[r][c] = button

        # Reset button
        self.reset_button = tk.Button(self.master, text="Reset Game", font=('Arial', 14),
                                      command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=15)

    def button_click(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player,
                                         fg="blue" if self.current_player == "X" else "red")

            if self.check_win():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                self.status_label.config(text="It's a Draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        player = self.current_player

        # Check rows
        for r in range(3):
            if all(self.board[r][c] == player for c in range(3)):
                return True
        # Check columns
        for c in range(3):
            if all(self.board[r][c] == player for r in range(3)):
                return True
        # Check diagonals
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
           (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        if not any("" in row for row in self.board) and not self.check_win():
            return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False

        self.status_label.config(text=f"Player {self.current_player}'s turn")

        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()