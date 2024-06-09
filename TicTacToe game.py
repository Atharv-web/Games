import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    label:str
    color:str

class Move(NamedTuple):
    row:int
    col:int
    label: str = ""
    
BOARD_SIZE = 3
DEFAULT_PLAYERS = (Player(label='X', color = 'red'),
                       Player(label="O", color = 'violet'),)

# getting the game logic
class TicTacToeGame:
    def __init__(self,players = DEFAULT_PLAYERS,board_size = BOARD_SIZE):
        self.game_players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.game_players)
        self.winner_combo = []
        self.current_moves = []
        self.has_winner = False
        self.winning_combos = []
        self.setup_board()

    def setup_board(self):
        self.current_moves = [
            [Move(row,col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self.winning_combos = self.get_winning_combos()

    def get_winning_combos(self):
        rows = [
            [(move.row,move.col) for move in row]
            for row in self.current_moves
        ]    
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        secind_diagonal = [col[j] for j,col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal,secind_diagonal]
    
    # validating the players move
    def is_valid_move(self,move):
        row, col = move.row, move.col
        move_was_not_played = self.current_moves[row][col].label =""
        no_winner = not self.has_winner
        return no_winner and move_was_not_played

    # check the players move to declare the winner
    def process_move(self,move):
        row,col = move.row,move.col
        self.current_moves[row][col] = move
        for combo in self.winning_combos:
            results = set(
                self.current_moves[n][m].label
                for n,m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self.has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self.has_winner
    
    def is_tied(self):
        no_winner = not self.has_winner
        played_moves = (
            move.label for row in self.current_moves for move in row
        )
        return no_winner and all(played_moves)

    def toggle_between_players(self):
        self.current_player = next(self.game_players)
    
    def reset_game(self):
        self.setup_board()
        self.has_winner = False
        self.winner_combo = []


# Class for creating the game board
class GameBoard(tk.Tk):
    def __init__(self,game):
        super().__init__()
        self.title("Tic Tac Toe Board Game")
        self._cells = {}
        self.game = game
        self.create_menu()
        self.create_board_grid()
        self.create_display()

    def reset_game(self):
        for row, row_content in enumerate(self.current_moves):
            for col,_ in enumerate(row_content):
                row_content[col] = Move(row,col)
        self.game.has_winner = False
        self.game.winner_combo = []

    def create_menu(self):
        menu_bar = tk.Menu(master = self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="play again",command = self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit",command = quit)
        menu_bar.add_cascade(label = "File",menu = file_menu)

    def reset_board(self):
        self.game.reset_game()
        self.update_display(msg ="Ready to Play again?")
        for button in self._cells.keys():
            button.config(highlightbackground= "lighblue")
            button.config(text="")
            button.config(fg = "black")

    def create_display(self):
        display_frame = tk.Frame(master=self) #creating a frame object
        display_frame.pack(fill=tk.X) #places the frame
        # we are creating a label object here
        self.display = tk.Label(master=display_frame,text="Are You Ready?", font=font.Font(size =24,weight="bold"))
        self.display.pack() #packs the display label

    def create_board_grid(self):
        grid_frame = tk.Frame(master = self)
        grid_frame.pack()
        for row in range(self.game.board_size):
            self.rowconfigure(row,weight=1,minsize=50)
            self.columnconfigure(row,weight=1,minsize =75)
            for col in range(self.game.board_size):
                button = tk.Button(master=grid_frame,text="",
                                font=font.Font(size = 36,weight='bold'),
                                fg='black', width=3, height=2, highlightbackground='lightblue')
                self._cells[button] = (row,col)
                button.bind("<Button-1>",self.play)
                button.grid(row=row,column=col,padx=5,pady=5,sticky='nsew')

    def play(self,event):
        clicked_button = event.widget
        row,col = self._cells[clicked_button]
        move = Move(row,col,self.game.current_player.label)
        if self.game.is_valid_move(move):
            self.update_button(clicked_button)
            self.game.process_move(move)
            if self.game.is_tied():
                self.update_display(msg = "Game Tied", color = 'Blue')
            elif self.game.has_winner():
                self.highlighting_cells()
                msg = f'Player"{self.game_current_player.label}" won!'
                color = self.game.current_player.color
                self.update_display(msg,color)
            else:
                self.game.toggle_between_players()
                msg = f"{self.game.current_player.label}'s turn"    
                self.update_display(msg)

    def update_button(self,clicked_button):
        clicked_button.config(text = self.game.current_player.label)
        clicked_button.config(fg = self.game.current_player.color)
    
    
    def update_display(self,msg,color = "black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def highlighting_cells(self):
        for button, coordinates in self.cells.items():
            if coordinates in self.game.winner_combo:
                button.config(highlightbackground = 'red')


def main():
    game = TicTacToeGame()
    board = GameBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()
