import unittest
import sudokuStandardBacktracking
import pandas as pd

class TestCalc(unittest.TestCase):
    #Use pandas to read all rows (cols:['quizzes','solutions'])
    puzzleDf = pd.read_csv('sudoku.csv', dtype='str', delimiter=',')

    answerstr = ""
    def test_0(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][0]), self.puzzleDf['solutions'][0], msg="Test Failed!")
    def test_1(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][1]), self.puzzleDf['solutions'][1], msg="Test Failed!")
    def test_2(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][2]), self.puzzleDf['solutions'][2], msg="Test Failed!")
    def test_3(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][3]), self.puzzleDf['solutions'][3], msg="Test Failed!")
    def test_4(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][4]), self.puzzleDf['solutions'][4], msg="Test Failed!")
    def test_5(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][5]), self.puzzleDf['solutions'][5], msg="Test Failed!")
    def test_6(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][6]), self.puzzleDf['solutions'][6], msg="Test Failed!")
    def test_7(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][7]), self.puzzleDf['solutions'][7], msg="Test Failed!")
    def test_8(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][8]), self.puzzleDf['solutions'][8], msg="Test Failed!")
    def test_9(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][9]), self.puzzleDf['solutions'][9], msg="Test Failed!")
    def test_10(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][10]), self.puzzleDf['solutions'][10], msg="Test Failed!")
    def test_11(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][11]), self.puzzleDf['solutions'][11], msg="Test Failed!")
    def test_12(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][12]), self.puzzleDf['solutions'][12], msg="Test Failed!")
    def test_13(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][13]), self.puzzleDf['solutions'][13], msg="Test Failed!")
    def test_14(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][14]), self.puzzleDf['solutions'][14], msg="Test Failed!")
    def test_15(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][15]), self.puzzleDf['solutions'][15], msg="Test Failed!")
    def test_16(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][16]), self.puzzleDf['solutions'][16], msg="Test Failed!")
    def test_17(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][17]), self.puzzleDf['solutions'][17], msg="Test Failed!")
    def test_18(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][18]), self.puzzleDf['solutions'][18], msg="Test Failed!")
    def test_19(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][19]), self.puzzleDf['solutions'][19], msg="Test Failed!")
    def test_20(self):
        self.assertEqual(sudokuStandardBacktracking.main(self.puzzleDf['quizzes'][20]), self.puzzleDf['solutions'][20], msg="Test Failed!")
        

if __name__ == '__main__':
    unittest.main()