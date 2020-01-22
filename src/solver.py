xyz = [
  [8,0,5,0,0,0,2,0,0],
  [0,0,0,0,0,6,8,0,0],
  [4,1,0,0,0,7,0,0,3],
  [0,7,3,6,0,8,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,2,0,4,5,3,0],
  [2,0,0,5,0,0,0,6,7],
  [0,0,9,1,0,0,0,0,0],
  [0,0,6,0,0,0,4,0,1]
]

class Sudoku_Solver:

  def __init__(self, board):
    self.board = board
    self.solve(self.board)

  def validity_check(self, board, num, coords):
    for i in range(len(board)):
      if board[coords[0]][i]==num and i!=coords[1]:
        return False
    for j in range(len(board)):
      if board[j][coords[1]]==num and j!=coords[0]:
        return False    
    box_x = coords[0] // 3
    box_y = coords[1] // 3
    for i in range(box_x*3, box_x*3+3):
      for j in range(box_y*3, box_y*3+3):
        if board[i][j]==num and i!=coords[0] and j!=coords[1]:
          return False
    return True

  def solve(self, board):
    coords = self.get_blanks(board)
    if coords is not None:
      for num in range(1, 10):
        if self.validity_check(board, num, coords):
          self.board[coords[0]][coords[1]] = num
          if self.solve(board):
            return True
          self.board[coords[0]][coords[1]] = 0  
      return False
    return True

  def print_board(self, board):
    for i in range(len(board)):
      if i%3==0 and i!=0:
        print('--------------------')
      for j in range(len(board)):
        if j%3==0 and j!=0:
          print('|', end='')
        if j == 8:
          print(board[i][j])
        else:
          print(str(board[i][j]) + ' ', end='')
  
  def get_blanks(self, board):
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j]==0:
          return (i, j)
    self.print_board(self.board)

Sudoku_Solver(xyz)
