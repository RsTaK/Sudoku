import numpy as np
import cv2
import string
import random

def randomString(length):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def approx(c):
  p = cv2.arcLength(c, True)
  return cv2.approxPolyDP(c, 0.02*p, True)

def convertSquare(image, default_size = 306):
	return cv2.resize(image, (default_size, default_size))

def loadImage(path):
  image = cv2.imread(path)
  if image is None:
    print('Sorry, No Image Found...')
  else:
    print('Image Loaded Sucessfully...')
    return image

def showImage(windowName, image):
  cv2.imshow(windowName, image)

def destroyWindows():
  k = cv2.waitKey(0)
  if k == 27:
    print('ESC Pressed ...')
    cv2.destroyAllWindows()

def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	return rect

def four_point_transform(image, pts):
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	return warped

def auto_canny(image, sigma=0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	return edged