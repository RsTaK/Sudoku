from keras.models import load_model
import cv2

class recognizeDigit:

  def __init__(self, cell):
    self.predict(cell)
  
  def predict(self, cell):
    model = load_model('./model/Model.h5')
    rescaled_cell = self.rescale(cell)
    pred = model.predict(rescaled_cell)
    print(pred.argmax())
  
  def rescale(self, cell):
    resized_cell = cv2.resize(cell, (28, 28))
    return resized_cell.reshape(1, resized_cell.shape[0], resized_cell.shape[1], 1)