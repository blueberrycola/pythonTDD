# pythonTDD
An application to test a simple backtracking algorithm of sudoku. Used to learn unit testing for python. 

Important Note: In order to run this program you must download the csv file found from kaggle. The file size is too big to put in github!
Dataset was pulled from kaggle.com 1,000,000 Sudoku puzzles + solution: (https://www.kaggle.com/datasets/bryanpark/sudoku)

# How its made:

First pandas pulls the csv file labeled sudoku inside sudokuTest.py.

Each row for the column labeled 'quizzes' inside the dataframe is parsed into a 2d list for the backtracking algorithm. 0's indicate an empty space for the puzzle column. Grid is filled from left to right.

Once grid list has been filled it is sent into the backtracking function.

Once the puzzle is solved it is parsed back into a string and compared to the string inside the solutions column of panda data frame.

If both the backtracking solution and original solution match the tests pass
