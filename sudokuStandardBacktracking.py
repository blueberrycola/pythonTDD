import pandas as pd
import unittest
#Parses 2d list back into string !!!USED for sudokuTest.py!!!
def parseList(puzzlelist):
    basestr = ""
    for r in puzzlelist:
        for element in r:
            basestr = basestr + str(element)
    return basestr
            
#Reads puzzle column inside csv file
def readAndParse(quizstr):
    grid = [[0 for i in range(9)] for j in range(9)] #Create 2d array
    i = 0
    j = 0
    for char in quizstr:    #Read each character inside the panda str
        grid[i][j] = int(char)   #Write to 2d list, convert char to integer
        if j == 8:
            j = 0
            i+=1
        else:
            j+=1
    

    return grid     #Return the 2d list


#Helper function for solverSudoku(), moves to next empty cell (when cell == 0)
def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1
#Helper function for solveSudoku(), returns true if row, column, and cube are valid for a given cell
def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False
#A standard backtracking algorithm, uses recursion.
def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True     #Returns corrected grid aswell
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False
def main(basestr):
    #Loop thru each entry and solve the puzzle using the backtracking algorithm
    quiz = readAndParse(basestr)
    solveSudoku(quiz, i=0, j=0)
    answerstr = parseList(quiz)
    return answerstr
