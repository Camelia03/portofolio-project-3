from random import randrange

# name_str = input("Enter your name:\n")
# print(f"Welcome to Battleships Game, {name_str}!")


class GameBoard:
    """
    Class representing the game board
    """

    def __init__(self) -> None:
        self.size = 4
        self.board_state = [
            [" " for i in range(self.size)] for i in range(self.size)]
        self.nr_boats = 1
        self.boat_positions = []
        for i in range(self.nr_boats):
            pos = self.gen_unique_position()
            self.boat_positions.append(pos)
            self.add_to_state(pos, "O")
        self.correct_guesses = []
        self.wrong_guesses = []

    def pretty_print(self):
        """
        Print the board
        """
        for i, row in enumerate(self.board_state):
            print(i, end=": ")
            for cell in row:
                print("|", end="")
                print(cell, end="")
            print("|")

    def gen_random_position(self):
        """
        Generate a random position
        """
        x = randrange(self.size)
        y = randrange(self.size)
        return (x, y)

    def gen_unique_position(self):
        """
        Generate a random unique position
        """
        while True:
            pos = self.gen_random_position()
            if pos not in self.boat_positions:
                return pos

            pos = self.gen_random_position()

    def add_guess(self, pos):
        """
        Check if the guess is a hit and add to board state
        """
        if pos in self.boat_positions:
            self.correct_guesses.append(pos)
            self.add_to_state(pos, "*")
        else:
            self.wrong_guesses.append(pos)
            self.add_to_state(pos, "X")

    def add_to_state(self, pos, character):
        """
        Set a character in the board state at a position
        """
        self.board_state[pos[0]][pos[1]] = character

    def gen_random_guess(self):
        """
        Generate a random unique position
        """
        while True:
            pos = self.gen_random_position()
            if pos not in self.wrong_guesses and pos not in self.correct_guesses:
                return pos

    def game_finished(self):
        """ The game is finished if the number of correct guesses
            is the same as the number of boats
        """
        return len(self.correct_guesses) == len(self.boat_positions)

    def validate_position(self, pos):
        """
        Check if the position is valid on the board
        """
        if len(pos) != 2:
            return False
        if pos[0] < 0 or pos[0] > 3:
            return False
        if pos[1] < 0 or pos[1] > 3:
            return False
        return True


def parse_user_guess(user_guess):
    """
    Function to parse user guess to tuple of int
    """
    return tuple(map(int, user_guess.split(",")))


def get_user_guess(board):
    """
    Ask the user for a guess
    Parse and validate the guess
    """
    while True:
        try:
            # Parse the user input to a tuple
            parsed_user_guess = parse_user_guess(
                input("Please enter a guess:"))
            if board.validate_position(parsed_user_guess) is True:
                return parsed_user_guess
        except ValueError:
            pass

        print("Please enter two numbers separated by a comma")


def play_round(user_board, computer_board):
    """
    Play a round of the game
    """
    while True:
        # Display the game boards
        print("Computer's board: ")
        computer_board.pretty_print()
        print("User's board: ")
        user_board.pretty_print()

        # Ask the user for correct guess
        user_guess = get_user_guess(computer_board)

        # Add the user's guess to the computer board and print the result
        computer_board.add_guess(user_guess)
        computer_board.pretty_print()

        # Check if the user has won
        if computer_board.game_finished():
            print("Congrats! You have won!")
            break

        # Generate randome guess for the computer
        computer_guess = user_board.gen_random_guess()

        # Add the computer's guess to the user's board and print the result
        user_board.add_guess(computer_guess)
        user_board.pretty_print()

        # Check if the computer has won
        if user_board.game_finished():
            print("Oh no! You have lost!")
            break


def run():
    """
    Main game loop
    """
    while True:
        # Generate game boards
        computer_board = GameBoard()
        user_board = GameBoard()

        # Run game round
        play_round(user_board, computer_board)

        print("Game finished")

        # Ask the user to play again
        play_again = input(
            "Would you like to play again? Press \"N\" to end or any key to play again\n")
        if play_again.lower() == "n":
            break


run()
