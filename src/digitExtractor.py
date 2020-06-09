import cv2
import numpy as np
from src import helper

from src.recognizeDigit import recognizeDigit

class digitExtractor:

  def __init__(self, path):

    self.image = path
    #self.image = helper.loadImage(path)
    gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 5, 250, 250)
    thresh  = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,7)
    #gridless_img = self.removeGrid(thresh)
    helper.showImage('Cropped Image',thresh)
    self._output = self.eachGrid(thresh)

  """
  def removeGrid(self, image):  
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros((self.image.shape),np.uint8)
    c = 0
    for i in contours:
      area = cv2.contourArea(i)
      if area<200:
        cv2.drawContours(mask, contours, c, (255, 255, 255), 1)
      c+=1
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    return mask
"""

  def eachGrid(self, image):
    width, height = image.shape
    cell_size = int(width / 9)
    count = 0
    each_row = list() 
    sudoku  = list()
    for w in range(0, width, cell_size):
      for h in range(0, height, cell_size):
        current_cell = image[w +5 : w + cell_size - 5, h + 5 : h + cell_size - 5]
        contours, _ = cv2.findContours(current_cell, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
          conts = sorted(contours, key=cv2.contourArea, reverse=True)
          cnt = conts[0]
          if cv2.contourArea(cnt)>cell_size*cell_size*0.03:
            #helper.showImage(helper.randomString(2),current_cell)
            #cv2.imwrite('src\digit detection\data2' + '\\' + helper.randomString(2) + '.jpg', current_cell)
            pred_digit = recognizeDigit(current_cell).prediction
          else:
            pred_digit = 0
        else:
          pred_digit = 0
        count+=1
        print('{} Numbers has been Recognized'.format(count))
        each_row.append(pred_digit)
        if len(each_row) == 9:
          sudoku.append(each_row)
          each_row = list() 
    return sudoku
  
  @property
  def output(self):
    return self._output
#digitExtractor('./input/cropped_Image.jpg')
