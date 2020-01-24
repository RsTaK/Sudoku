import helper
import cv2
x = [[9, 3, 6, 5, 4, 7, 2, 8, 1], [2, 1, 8, 6, 9, 3, 7, 4, 5], [7, 4, 5, 8, 2, 1, 6, 3, 9], [4, 7, 2, 1, 3, 8, 5, 9, 6], [6, 8, 3, 7, 5, 9, 4, 1, 2], [1, 5, 9, 2, 6, 4, 3, 7, 8], [5, 9, 7, 4, 1, 6, 8, 2, 3], [8, 2, 1, 3, 7, 5, 9, 6, 4], [3, 6, 4, 9, 8, 2, 1, 5, 7]]

class AR:
  
  def __init__(self, image, data):
    data = x
    image = helper.loadImage(r'input\cropped_Image.jpg')
    self.i = 0
    self.j = 0
    self.ARs(image, data)
    helper.destroyWindows()
    
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
            #self.display_Number(current_cell, data)
            self.j += 1
          else:
            self.display_Number(current_cell, data)
        else:
          self.display_Number(current_cell, data)
    helper.showImage("Solved Sudoku", thresh)

  def display_Number(self, current_cell, data):
    if self.j >= 9:    
      self.i += 1
      self.j = 0
    digit = data[self.i][self.j]
    print(self.i, self.j, digit)
    self.j += 1
'''    
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
    
    '''
AR(1,2)