import os
os.system("clear")
from model.Board import Board

class Engine:
    
    def initialise_board(self):
        self.board = Board()




    def is_valid_input(self,splitted_string):
        """Checks for validity of input"""
        if len(splitted_string) != 2:
            return False
        for splits in splitted_string:
            if not splits.isnumeric() or ((int(splits)<1) or (int(splits)>self.board.side_length)):
                return False
        return True




    def correctify_input(self,position):
        """Removes leading and trailing spaces for both inputs (r,c)"""
        splitted_string = position.split(",") #splits input string into rows and columns
        new_splitted_string = []
        for splits in splitted_string:
            new_split = splits.strip() #removes leading and trailing spaces to handle malign input
            new_splitted_string.append(new_split)

        return new_splitted_string




    def get_Position(self,player):
        """Gets absolute position to place X or O for both players. Returns 0 for invalid input"""

        position = input(f"\n For {player}) Please choose position in the form (row,col) > ")
        
        splitted_string = self.correctify_input(position)
        if self.is_valid_input(splitted_string):
            
            absolute_position = (self.board.side_length *((int(splitted_string[0]))-1)) + (int(splitted_string[1]))
            return absolute_position
        else:
            return 0






    def play(self):
        """Starts the game"""
        self.initialise_board()

        while True:
            self.board.refresh_screen()
            x_choice = self.get_Position("X")

            if x_choice == 0:      #restarts game if invalid input
                raise ValueError("Invalid input")
                # self.board.reset()
                # continue
            

            while self.board.is_occupied(x_choice): #loop until an input found which is not already filled
                print("Given position is already filled!")
                x_choice = self.get_Position("X")
                
            self.board.update_cell(x_choice,"X")                      
            self.board.refresh_screen()

            if self.board.is_winner("X"):  #check for X win
                print("\nX has won the match!\n")
                play_again = input("Would you like to play again? [Y/N] > ").upper()
                if play_again == "Y":
                    self.board.reset()
                    continue
                else:
                    break

            if self.board.is_tied():  #check for tied match
                print("\nGame tied.\n")
                play_again = input("Would you like to play again? [Y/N] > ").upper()
                if play_again == "Y":
                    self.board.reset()
                    continue
                else:
                    break
            
            o_choice = self.get_Position("O")
            
            if o_choice == 0: #restarts game if invalid input
                raise ValueError("Invalid input")
                # print("Invalid input. Game restarting!")
                # self.board.reset()
                # continue

            while self.board.is_occupied(o_choice):  #loop until an input found which is not already filled
                print("Given position is already filled!")
                o_choice = self.get_Position("O")
               

            self.board.update_cell(o_choice,"O")
            self.board.refresh_screen()

            if self.board.is_winner("O"):  #check for O win
                print("\nO has won the match!\n")
                play_again = input("Would you like to play again? [Y/N] > ").upper()
                if play_again == "Y":
                    self.board.reset()
                    continue
                else:
                    break

            if self.board.is_tied():   #check for tied match
                print("\nGame tied.\n")
                play_again = input("Would you like to play again? [Y/N] > ").upper()
                if play_again == "Y":
                    self.board.reset()
                    continue
                else:
                    break


