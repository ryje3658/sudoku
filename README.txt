Ryan Jensen
CS 325 - Portfolio Sudoku Project
2/23/2021

To run the program first 'pip install termcolor' to install the library 'termcolor' which allows colored text to be
outputted to the terminal. This makes the game much clearer to play for the user. Then type 'python3 sudoku.py' to run
the game with a starting board. That will allow you to play the game. Below are the rules to play the game, which are
printed to the terminal when the program is started.


To test that the code works to identify a winning board using the algorithm, without playing
the full game, go into the __main__ function in sudoku.py and comment out the play_game(easy_start_board)
and uncomment the play_game(winning_board). (Note that this is simply changing the input board from
a standard starting board, to an already complete board, so it triggers the game to evaluate the
board's correctness.


HOW TO PLAY:
Squares colored in magenta are part of the starting board and unchangeable. Any other squares
can be changed by entering a number between 1 and 9, and then the space of the grid you'd like
to place that number in according the values on the x and y axis, in form 'B3'. At any time,
enter 'x' as input (in either the number to put in square input or the coordinate input) and the game will exit.
Once all squares are filled in, the game will check automatically if the solution is valid.