import cv2
import helper
images = helper.loadImage(r'input\cropped_Image.jpg')
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 5, 250, 250)
image  = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,7)
helper.showImage('test1', image)
width, height = image.shape
cell_size = int(width / 9)
count = 0
'''for w in range(0, width, cell_size):
  for h in range(0, height, cell_size):
  '''
current_cell = image[0 +5 : 0 + cell_size - 5, cell_size +cell_size +cell_size + 5 :cell_size + cell_size +cell_size + cell_size - 5]
helper.showImage('test', current_cell)
helper.destroyWindows()
