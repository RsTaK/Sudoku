import cv2
import numpy as np
import helper


'''
  File used to extract grid and pickle the cropped / area of interest 
'''

class gridExtractor:

  def __init__(self, path):
    self.image = helper.loadImage(path)
    processed_image = self.preprocess(self.image)
    self.croppedImage(processed_image)
    helper.destroyWindows()

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
    
    masked_Image = cv2.drawContours(self.image.copy(),[target],0,(0,255,0), -1)
    helper.showImage('Masked Image', masked_Image)
    cropped_Image = helper.four_point_transform(self.image, target)
    cropped_Image = helper.convertSquare(cropped_Image)
    helper.showImage('Cropped Image', cropped_Image)
    cv2.imwrite('./input/cropped_Image1.jpg', cropped_Image)
    print('Grid Extracted...')
    