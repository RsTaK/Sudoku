import cv2
import numpy as np
import helper
from gridExtractor import gridExtractor
from recognizeDigit import recognizeDigit

class digitExtractor:

  def __init__(self, path):
    self.image = helper.loadImage(path)
    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    self.image = cv2.bilateralFilter(self.image, 5, 150, 150)
    self.image  = cv2.adaptiveThreshold(self.image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,4)
    helper.showImage('Cropped Image',self.image)
    self.eachGrid(self.image)
    #helper.showImage('Counter Image',self.image)
    helper.destroyWindows()
  
  def eachGrid(self, image):
    width, height= image.shape
    cell_size = int(width / 9)
    print(cell_size)
    count = 0
    for w in range(0, width, cell_size):
      for h in range(0, height, cell_size):
        current_cell = image[w+5 : w + cell_size-5, h+5 : h + cell_size-5]
        contours, _ = cv2.findContours(current_cell, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
          count+=1
          recognizeDigit(current_cell)
        
    print(count)

digitExtractor('./input/cropped_Image1.jpg')