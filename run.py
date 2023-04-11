# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randrange

# name_str = input("Enter your name:\n")
# print(f"Welcome to Battleships Game, {name_str}!")


class GameBoard:
    def __init__(self) -> None:
        self.size = 4
        self.board_state = [
            [" " for i in range(self.size)] for i in range(self.size)]
        self.nr_boats = 3
        self.boat_positions = []
        for i in range(self.nr_boats):
            pos = self.gen_unique_position()
            self.boat_positions.append(pos)
            self.board_state[pos[0]][pos[1]] = "O"

    def pretty_print(self):
        for i, row in enumerate(self.board_state):
            print(i, end=": ")
            for cell in row:
                print("|", end="")
                print(cell, end="")
            print("|")

    def gen_random_position(self):
        x = randrange(self.size)
        y = randrange(self.size)
        return (x, y)

    def gen_unique_position(self):
        while True:
            pos = self.gen_random_position()
            print(pos)
            if pos not in self.boat_positions:
                return pos

            pos = self.gen_random_position()


board = GameBoard()
board.pretty_print()
