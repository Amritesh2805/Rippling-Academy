
from TicTacToeBoardGame import TicTacToeBoardGame
import os

class Board(TicTacToeBoardGame):
    
    def __init__(self):
        self.side_length = 3
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("---|---|---")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("---|---|---")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")
    
    def update_cell(self,cell_number,player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number]=player

    def is_occupied(self,cell_number):
        if self.cells[cell_number] == " ":
            return False
        else:
            return True

    def is_winner(self,player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True
        elif self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            return True
        elif self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            return True
        elif self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        elif self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True
        elif self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            return True
        elif self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            return True
        elif self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            return True

        return False
        

    def is_tied(self):
        filled_cells = 0
        for cell in self.cells:
            if cell != " ":
                filled_cells+=1

        if filled_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def refresh_screen(self):
        os.system("clear")
        self.print_header()
        self.display()