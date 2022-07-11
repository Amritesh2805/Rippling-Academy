
from model.TicTacToeBoardGame import TicTacToeBoardGame
import os

class Board(TicTacToeBoardGame):
    
    def __init__(self):
        """Initialises board with custom side length"""
        """User can play tic tac toe of any side length"""
        self.side_length = 4
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
        """Checks for a row victory"""
        result = False
        for rows in range(1,self.side_length+1):
            b = True
            for cols in range(1,self.side_length+1):
                if self.cells[(self.side_length*(rows-1))+cols] == player:
                    b = b and True
                else:
                    b = b and False

            result = result or b
        return result

    def column_victory(self,player):
        """Checks for a column victory"""
        result = False
        for cols in range(1,self.side_length+1):
            b = True
            for rows in range(1,self.side_length+1):
                if self.cells[(self.side_length*(rows-1))+cols] == player:
                    b = b and True
                else:
                    b = b and False

            result = result or b
        return result

    def diagonal_victory(self,player):
        """Checks for a diagonal victory"""
        result = False
        b = True
        for rows in range(1,self.side_length+1):
            if self.cells[(self.side_length*(rows-1))+rows] == player:
                b = b and True
            else:
                b = b and False
            
        result = result or b
        b = True
        for rows in range(1,1+self.side_length):
            if self.cells[(self.side_length*(rows-1))+(self.side_length-rows+1)] == player:
                b = b and True
            else:
                b = b and False
        
        result = result or b

        return result
        




    def is_winner(self,player):
        """Checks if any of the 3 types of victories present"""
        if self.row_victory(player) or self.column_victory(player) or self.diagonal_victory(player):
            return True
        else:
            return False


        
        

    def is_tied(self):
        """Checks for tied match"""
        filled_cells = 0
        for cell in self.cells:
            if cell != " ":
                filled_cells+=1

        if filled_cells == (self.side_length*self.side_length):
            return True
        else:
            return False




    def reset(self):
        """Resets the board"""
        self.cells = [" "]*((self.side_length*self.side_length)+1)




    def refresh_screen(self):
        """Refreshes screen after an input"""
        os.system("clear")
        self.print_header()
        self.display()