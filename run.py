# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#name_str = input("Enter your name:\n")
#print(f"Welcome to Battleships Game, {name_str}!")

class GameBoard:
    def __init__(self) -> None:
        self.board_state = [[" " for i in range(4)] for i in range(4)]

    def pretty_print(self):
       for row in self.board_state:
        for cell in row:
            print("|_", end="")
        print("|")


board = GameBoard()
board.pretty_print()




        