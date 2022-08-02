# pythonTDD
An application to test a simple backtracking algorithm of sudoku. Used to learn unit testing for python. 

Important Note: In order to run this program you must download the csv file found from kaggle. The file size is too big to put in github!
Dataset was pulled from kaggle.com 1,000,000 Sudoku puzzles + solution: (https://www.kaggle.com/datasets/bryanpark/sudoku)

# How its made:

First pandas pulls the csv file labeled sudoku.
The columns labeled puzzle and solution are each their own variable

For both the data containing puzzle and solution information it is parsed
by a string into a 9x9 2d list. 0's indicate an empty space for the puzzle column.

Once the backtracking algorithm has finished it is turned back into a 81 character string and compared to the solution with a unit test
