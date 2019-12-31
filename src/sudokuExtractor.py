import cv2
import numpy as np
import helper


'''
  File used to extract grid and pickle the cropped / area of interest 
'''

class Extractor:

  def __init__(self, path):
    self.image = self.loadImage(path)
    processed_image = self.preprocess(self.image)
    cropped_Image = self.croppedImage(processed_image)
    self.destroyWindows()

  def loadImage(self, path):
    image = cv2.imread(path)
    if image is None:
      print('Sorry, No Image Found...')
    else:
      print('Image Loaded Sucessfully...')
      return image

  def preprocess(self, image):
    print('Preprocessing has been started...')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    thresh  = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,4)
    print('Preprocessing done sucessfully...')
    return thresh

  def croppedImage(self, image):
    print('Extracting Grid...')
    countors, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countor = sorted(countors, key = cv2.contourArea, reverse=True)
    for c in countor:
      approx = helper.approx(c)
      if len(approx) == 4:
        target = approx.reshape(4,2)
        break
    print()
    masked_Image = cv2.drawContours(self.image.copy(),[target],0,(0,255,0), -1)
    self.showImage('Masked Image', masked_Image)
    cropped = helper.four_point_transform(self.image, target)
    self.showImage('Cropped Image', cropped)
    print('Grid Extracted...')

  def showImage(self, windowName, image):
    cv2.imshow(windowName, image)

  def destroyWindows(self):
    self.k = cv2.waitKey(0)
    if self.k == 27:
      print('ESC Pressed ...')
      cv2.destroyAllWindows()

Extractor('./input/sudoku.jpg')