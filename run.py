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
            self.add_to_state(pos, "O")
        self.correct_guesses = []
        self.wrong_guesses = []

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
            if pos not in self.boat_positions:
                return pos

            pos = self.gen_random_position()

    def add_guess(self, pos):
        if pos in self.boat_positions:
            self.correct_guesses.append(pos)
            self.add_to_state(pos, "*")
        else:
            self.wrong_guesses.append(pos)
            self.add_to_state(pos, "X")

    def add_to_state(self, pos, character):
        self.board_state[pos[0]][pos[1]] = character

    def gen_random_guess(self):
        while True:
            pos = self.gen_random_position()
            if pos not in self.wrong_guesses and pos not in self.correct_guesses:
                return pos


computer_board = GameBoard()
user_board = GameBoard()

while True:
    print("Computer's board: ")
    computer_board.pretty_print()
    print("User's board: ")
    user_board.pretty_print()

    user_guess = input("Please enter a guess:")
    parsed_used_guess = tuple(map(int, user_guess.split(",")))
    print(parsed_used_guess)
    computer_board.add_guess(parsed_used_guess)
    computer_board.pretty_print()

    computer_guess = user_board.gen_random_guess()
    user_board.add_guess(computer_guess)
    user_board.pretty_print()
