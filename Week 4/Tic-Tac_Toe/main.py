import os
os.system("clear")
from Board import Board

board = Board()

def getPosition(player):
    position = input(f"\n For {player}) Please choose position in the form (row,col) > ")
    if len(position) == 3 and position[0].isnumeric() and position[2].isnumeric() and position[1]==',':
        absolute_position = (board.side_length *((int(position[0]))-1)) + (int(position[2]))
        return absolute_position

def main():

    while True:
        board.refresh_screen()
        x_choice = getPosition("X")
        

        while board.is_occupied(x_choice):
            print("Given position is already filled!")
            x_choice = getPosition("X")
            
            

        board.update_cell(x_choice,"X")
        
        
        board.refresh_screen()

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
        
        o_choice = getPosition("O")
        

        while board.is_occupied(o_choice):
            print("Given position is already filled!")
            o_choice = getPosition("O")
            

        board.update_cell(o_choice,"O")

        board.refresh_screen()

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

if __name__ == "__main__":
    main()
