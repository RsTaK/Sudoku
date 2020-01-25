import helper
import argparse
from AR import AR
from solver import Sudoku_Solver
from gridExtractor import gridExtractor
from digitExtractor import digitExtractor
import sys


if __name__ == "__main__":
  print(sys.argv[1])
  cropped_Image = gridExtractor(sys.argv[1]).output
  recognized_sudoku = digitExtractor(cropped_Image).output
  solved_sudoku = Sudoku_Solver(recognized_sudoku).output
  AR(cropped_Image, solved_sudoku)
  helper.destroyWindows()