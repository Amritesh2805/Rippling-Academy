
from TicTacToeBoardGame import TicTacToeBoardGame
import os

class Board(TicTacToeBoardGame):
    
    def __init__(self):
        """Initialises board with custom side length"""
        self.side_length = 3
        self.cells = [" "]*((self.side_length*self.side_length)+1)



    def display(self):
        """Displays board on the command line"""
        self.cells_iterator = 1
        for rows in range(1,self.side_length):
            for cols in range(1,self.side_length):
                print(f" {self.cells[self.cells_iterator]} |",end="")
                self.cells_iterator+=1
            print(f" {self.cells[self.cells_iterator]} ")
            self.cells_iterator+=1
            print((self.side_length-1)*"---|",end="")
            print("---")
        
        for cols in range(1,self.side_length):
            print(f" {self.cells[self.cells_iterator]} |",end="")
            self.cells_iterator+=1
        print(f" {self.cells[self.cells_iterator]} ")
                           
    

    def update_cell(self,cell_number,player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number]=player



    def is_occupied(self,cell_number):
        if self.cells[cell_number] == " ":
            return False
        else:
            return True

    
    def row_victory(self,player):
        pass



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

        if filled_cells == (self.side_length*self.side_length):
            return True
        else:
            return False



    def reset(self):
        self.cells = [" "]*((self.side_length*self.side_length)+1)



    def refresh_screen(self):
        os.system("clear")
        self.print_header()
        self.display()