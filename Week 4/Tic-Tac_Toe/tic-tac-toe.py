import os
os.system("clear")

class BoardGame:
    def print_header(self):
        print("Welcome to a board game")

class TicTacToeBoardGame(BoardGame):
    def print_header(self):
        print("Welcome to Tic-Tac_Toe!")


class Board(TicTacToeBoardGame):
    def __init__(self):
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
            return False
        else:
            return True

    # def is_winner(self,player):
    #     for winning_situations in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
    #         result=True
    #         for cell_number in winning_situations:
    #             if self.cells[cell_number]!=player:
    #                 return False
            
    #         if result==True:
    #             return True
        
    #     return False

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


board = Board()
n = 3

def refresh_screen():
    os.system("clear")
    board.print_header()
    board.display()

while True:
    refresh_screen()

    x_choice_string = input("\nFor X) Please choose position. > ")
    x_choice = (n*((int(x_choice_string[0]))-1)) + (int(x_choice_string[2]))
    already_present = board.update_cell(x_choice,"X")
    if already_present:
        continue
    
    refresh_screen()

    if board.is_winner("X"):
        print("\nX has won the match!\n")
        play_again = input("Would you like to play again? [Y/N] > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tied():
        print("\nGame tied.\n")
        play_again = input("Would you like to play again? [Y/N] > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
    o_choice_string = input("\nFor O) Please choose position. > ")
    o_choice = (n*((int(o_choice_string[0]))-1)) + (int(o_choice_string[2]))
    already_present = board.update_cell(o_choice,"O")

    
    refresh_screen()

    if board.is_winner("O"):
        print("\nO has won the match!\n")
        play_again = input("Would you like to play again? [Y/N] > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tied():
        print("\nGame tied.\n")
        play_again = input("Would you like to play again? [Y/N] > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

