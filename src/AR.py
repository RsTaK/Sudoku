from src import helper
import cv2

class AR:
  
  def __init__(self, image, data):

    self.i = 0
    self.j = 0
    self.ARs(image, data)
    
  def ARs(self, image, data): 
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 5, 250, 250)
    thresh  = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,7)
    width, height = thresh.shape
    cell_size = int(width / 9)

    for w in range(0, width, cell_size):
      for h in range(0, height, cell_size):
        current_cell = thresh[w +5 : w + cell_size - 5, h + 5 : h + cell_size - 5]
        contours, _ = cv2.findContours(current_cell, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
          conts = sorted(contours, key=cv2.contourArea, reverse=True)
          cnt = conts[0]

          if cv2.contourArea(cnt)>cell_size*cell_size*0.03:
            self.j+=1
            self.check()

          else:           
            self.display_Number(current_cell, data)
            self.j+=1
            self.check()

        else:
          self.display_Number(current_cell, data)
          self.j+=1
          self.check()
    cv2.imwrite('./static/upload/solved_Image.jpg', thresh)
    #helper.showImage("Solved Sudoku", thresh)
  
  def check(self):
    if self.j >=9:
      self.j = 0
      self.i += 1

  def display_Number(self, current_cell, data):

    digit = data[self.i][self.j]

    if digit == 1:
      cv2.putText(current_cell, str(1), (((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 2:
      cv2.putText(current_cell, str(2), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 3:
      cv2.putText(current_cell, str(3), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 4:
      cv2.putText(current_cell, str(4), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 5:
      cv2.putText(current_cell, str(5), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 6:
      cv2.putText(current_cell, str(6), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 7:
      cv2.putText(current_cell, str(7), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 8:
      cv2.putText(current_cell, str(8), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if digit == 9:
      cv2.putText(current_cell, str(9), ((current_cell.shape[1]-current_cell.shape[0])//2, (current_cell.shape[0]+current_cell.shape[1])//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
  