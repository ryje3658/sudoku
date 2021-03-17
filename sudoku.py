from termcolor import cprint, colored
from starting_sudoku_boards import winning_board, easy_start_board

class Board:

    def __init__(self):
        self.board = [0] * 81  # Initialize 81 empty squares in Sudoku board
        self.starting_squares = []  # Indices of numbers on starting board - user cannot change these squares

        # List of indices for each row in the sudoku board
        self.rows = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49, 50, 51, 52, 53],
            [54, 55, 56, 57, 58, 59, 60, 61, 62],
            [63, 64, 65, 66, 67, 68, 69, 70, 71],
            [72, 73, 74, 75, 76, 77, 78, 79, 80]
        ]

        # List of indices for each column in the sudoku board
        self.columns = [
            [0, 9, 18, 27, 36, 45, 54, 63, 72],
            [1, 10, 19, 28, 37, 46, 55, 64, 73],
            [2, 11, 20, 29, 38, 47, 56, 65, 74],
            [3, 12, 21, 30, 39, 48, 57, 66, 75],
            [4, 13, 22, 31, 40, 49, 58, 67, 76],
            [5, 14, 23, 32, 41, 50, 59, 68, 77],
            [6, 15, 24, 33, 42, 51, 60, 69, 78],
            [7, 16, 25, 34, 43, 52, 61, 70, 79],
            [8, 17, 26, 35, 44, 53, 62, 71, 80]
        ]

        # Lists of indices for each 'square' in the sudoku board
        self.squares = [
            [0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]
        ]

    @staticmethod
    def print_rules():
        """Prints the rules to the game."""
        cprint("----- SUDOKO -----", "yellow")
        cprint("Squares colored in magenta are part of the starting board and unchangeable. Any other squares\n"
               "can be changed by entering a number between 1 and 9, and then the space of the grid you'd like\n"
               "to place that number in according the values on the x and y axis, in form 'B3'. At any time, \n"
               "enter 'x' as input and the game will exit. Once all squares are filled in, the game will check\n"
               "automatically if the solution is valid.\n", "blue")

    def print_board(self):
        """Prints board to terminal in readable form with letters and numbers to display grid coordinates. Squares of
        starting board are colored in magenta for duration of game, to indicate to user they cannot be changed."""
        # Prints the x coordinate grid
        cprint("   A  B  C  D  E  F  G  H  I", 'cyan')

        index = 0
        for i in self.board:
            # Printing the grid numbers of the y axis colored cyan for visual clarity
            if index in [0, 9, 18, 27, 36, 45, 54, 63, 72]:
                if index == 0:
                    text = colored(1, "cyan")
                elif index == 9:
                    text = colored(2, "cyan")
                elif index == 18:
                    text = colored(3, "cyan")
                elif index == 27:
                    text = colored(4, "cyan")
                elif index == 36:
                    text = colored(5, "cyan")
                elif index == 45:
                    text = colored(6, "cyan")
                elif index == 54:
                    text = colored(7, "cyan")
                elif index == 63:
                    text = colored(8, "cyan")
                elif index == 72:
                    text = colored(9, "cyan")
                print(text, end="  ")

            # Squares that are part of starting board and unchangeable are colored magenta for clarity, otherwise normal
            if index in self.starting_squares:
                text = colored(i, "magenta")
                print(text, end="  ")
            else:
                print(i, end="  ")

            # Prints new lines every 9 squares
            if index in [8, 17, 26, 35, 44, 53, 62, 71]:
                print("")

            index += 1

        print("\n")

    def set_board(self, new_board):
        """Sets the game board using values inputted in list form."""
        self.board = new_board

        # Iterate over board, adding indices that have numbers in them to the starting squares attribute- unchangeable
        index = 0
        for space_value in self.board:
            if space_value != 0:
                self.starting_squares.append(index)
            index += 1

    def check_for_completion(self):
        """Checks if every square in the sudoku board is filled in."""
        if 0 not in self.board:
            return True
        else:
            return False

    def check_if_correct(self):
        """Algorithm that checks for correct solution to sudoku puzzle."""
        correct_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Check each of the 9 rows to make sure each row has 1, 2, 3, 4, 5, 6, 7, 8, and 9 (correct row)
        for row in self.rows:
            check = []
            for space in row:
                check.append(int(self.board[space]))
            if set(correct_numbers) == set(check):
                pass
            else:
                return False

        # Check each of the 9 columns to make sure each columns has 1, 2, 3, 4, 5, 6, 7, 8, and 9 (correct column)
        for column in self.columns:
            check = []
            for space in column:
                check.append(int(self.board[space]))
            if set(correct_numbers) == set(check):
                pass
            else:
                return False

        # Check each of the 9 squares to make sure each square has 1, 2, 3, 4, 5, 6, 7, 8, and 9 (correct square)
        for square in self.squares:
            check = []
            for space in square:
                check.append(int(self.board[space]))
            if set(correct_numbers) == set(check):
                pass
            else:
                return False

        # Since all rows, columns, and squares are valid, solution is valid
        return True

    def place_number(self, space, num):
        """Places number on sudoku board according to user input."""
        letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

        # Bad input check for letter coordinate in space coordinate
        if space[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            cprint("Error with letter in space coordinate. Please use capital letter A-I!", "red")
            return
        # Bad input check for number coordinate in space coordinate
        elif int(space[1]) not in range(1, 10):
            cprint("Error with number in space coordinate. Please use a number 1-9!", "red")
            return
        # Bad input check for number to place in square
        elif int(num) not in range(1, 10):
            cprint("Error with number to place. Please use a number 1-9!", "red")
            return
        # No errors- place number in space
        else:
            # Conversion of user input to list index
            row = self.rows[int(space[1]) - 1]
            board_index = row[letter_to_num[space[0]]]

            # Check if space is one of the starting number spaces and therefore unchangeable by user
            if board_index in self.starting_squares:
                cprint("Cannot change this square's value! It is a starting square.", "red")
                return

            # All error checking and conversions done - place number in square
            self.board[board_index] = int(num)


def play_game(starting_board):
    """Sets up a blank sudoku board to play. Gets user input to put numbers on the board and checks for a win."""
    # Initialize game and set board according to input
    game = Board()
    game.set_board(starting_board)
    game.print_rules()
    while True:
        game.print_board()
        cprint("If you'd like to exit, enter 'x' during either input prompt.", "cyan")
        if game.check_for_completion():
            if game.check_if_correct():
                cprint("Board is correct! You won!\n", "green")
                break
            else:
                cprint("Incorrect solution!\n", "red")
                break
        number_input = input("Please enter a number between 1 and 9 to place in a square: ")
        if number_input == 'x':
            cprint("Exiting...", "red")
            break
        space_input = input("Please enter a space to place number in from 'A1': ")
        if space_input == 'x':
            cprint("Exiting...", "red")
            break
        game.place_number(space_input, number_input)


if __name__ == '__main__':
    play_game(easy_start_board)
    # You can comment out the above line and uncomment this line to check a sample complete board for correctness. The
    # contents of this board are in the other file.
    # play_game(winning_board)
