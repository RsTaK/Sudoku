import helper
import argparse
from AR import AR
from solver import Sudoku_Solver
from gridExtractor import gridExtractor
from digitExtractor import digitExtractor

if __name__ == "__main__":

  cropped_Image = gridExtractor(r'input\sudoku.jpg').output
  recognized_sudoku = digitExtractor(cropped_Image).output
  solved_sudoku = Sudoku_Solver(recognized_sudoku).output
  AR(cropped_Image, solved_sudoku)
  helper.destroyWindows()