from random import randrange


class GameBoard:
    """
    Class representing the game board
    """

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

    def pretty_print(self, hide_boats=False):
        """
        Print the board using unicode characters
        """
        def hide_boat(cell):
            """
            Hide the boat if necessary
            """
            if hide_boats is True and cell == "O":
                return " "
            return cell

        table = ""
        for i, row in enumerate(self.board_state):
            # Print start of table
            if i == 0:
                table += "┏━━━" + "┳━━━" * (self.size - 1) + "┓" + "\n"

            # Print cells

            table += (
                "".join(f"┃ {hide_boat(cell)} " for cell in row) + "┃" + "\n"
            )

            # Print end or middle of table
            if i == len(self.board_state) - 1:
                table += "┗━━━" + "┻━━━" * (self.size - 1) + "┛" + "\n"
            else:
                table += "┣━━━" + "╋━━━" * (self.size - 1) + "┫" + "\n"

        print(table)

    def gen_random_position(self):
        """
        Generate a random position
        """
        row = randrange(self.size)
        col = randrange(self.size)
        return (row, col)

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
            if (pos not in self.wrong_guesses
                    and pos not in self.correct_guesses):
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
        if pos[0] < 0 or pos[0] > self.size - 1:
            return False
        if pos[1] < 0 or pos[1] > self.size - 1:
            return False
        return True

    def is_guess_unique(self, pos):
        """
        Check if the guess is unique(not previously guessed)
        """
        return (
            pos not in self.correct_guesses and pos not in self.wrong_guesses
        )


class BattleshipsGame:
    """
    Class representing the game
    """

    def __init__(self) -> None:
        self.user_name = ""

    def parse_user_guess(self, user_guess):
        """
        Function to parse user guess to tuple of int
        """
        return tuple(map(int, user_guess.split(",")))

    def get_user_guess(self, board):
        """
        Ask the user for a guess
        Parse and validate the guess
        """
        while True:
            try:
                # Parse the user input to a tuple
                parsed_user_guess = self.parse_user_guess(
                    input("Enter a guess: \n"))

                if board.validate_position(parsed_user_guess) is True:
                    if board.is_guess_unique(parsed_user_guess):
                        return parsed_user_guess
                    print("You already guessed this position.Try another one:")
                else:
                    print("Enter a position inside the board")
            except ValueError:
                pass

            print("Please enter two numbers separated by a comma")

    def play_round(self, user_board, computer_board):
        """
        Play a round of the game
        """
        def display_boards():
            """
            Display the game boards
            """
            print("Computer's board: ")
            computer_board.pretty_print(True)
            print(f"{self.user_name}'s board: ")
            user_board.pretty_print()

        while True:
            display_boards()

            # Ask the user for correct guess
            user_guess = self.get_user_guess(computer_board)

            # Add the user's guess to the computer board and print the result
            computer_board.add_guess(user_guess)

            # Check if the user has won
            if computer_board.game_finished():
                display_boards()
                print(f"Congrats, {self.user_name}! You have won!")
                break

            # Generate randome guess for the computer
            computer_guess = user_board.gen_random_guess()

            # Add the computer's guess to the user's board and print the result
            user_board.add_guess(computer_guess)

            # Check if the computer has won
            if user_board.game_finished():
                display_boards()
                print("Oh no! You have lost!")
                break

    def print_rules(self):
        """
        Print the game rules
        """
        print(("The rules are simple: "
               "Each player starts with three boats "
               "randomly positioned on his board."))
        print(("Then each round you have to make a guess "
               "to try and hit one of the opponents boat."))
        print(("The computer will also try "
               "to guess the location of your boats."))
        print(("The game ends when one player guesses "
               "the positions of all of their opponents boats."))
        print("Every guess must look like this: row,col")
        print("Example: 2,1")
        print("")

    def run(self):
        """
        Main game loop
        """
        while True:
            self.user_name = input("Enter your name:\n").strip()
            if self.user_name == "":
                print("Name cannot be empty")
            else:
                break

        print(f"Welcome to Battleships Game, {self.user_name}!")
        self.print_rules()
        while True:
            # Generate game boards
            computer_board = GameBoard()
            user_board = GameBoard()

            # Run game round
            self.play_round(user_board, computer_board)

            print("Game finished")

            # Ask the user to play again
            play_again = input(
                "Would you like to play again? Press \"N\"\
                     to end or any key to play again\n")
            if play_again.lower() == "n":
                break


game = BattleshipsGame()
game.run()
