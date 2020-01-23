from keras.models import load_model
import cv2
import pickle
import keras.backend as K
import numpy as np

'''def predict(self, cell):
  model = load_model('./model/Model.h5')
  f = K.function([model.layers[0].input, K.learning_phase()],[model.layers[-1].output])
  rescaled_cell = self.rescale(cell)

  result = []

  for _ in range(10):
      result.append(f([rescaled_cell, 1]))

  result = np.array(result)

  prediction = result.mean(axis=0)
  uncertainty = result.var(axis=0)
  if uncertainty.argmax() > 3:
    new_prediction = 0
    print(prediction.argmax(),uncertainty.argmax(),new_prediction)
  else:
    print(prediction.argmax(),uncertainty.argmax())'''  
class recognizeDigit:

  def __init__(self, cell):
    self._prediction = self.predict(cell)

  def predict(self, cell):
    model = load_model('./model/Model.h5')
    rescaled_cell = self.rescale(cell)
    pred = model.predict(rescaled_cell)
    return pred.argmax()

  def rescale(self, cell):
    resized_cell = cv2.resize(cell, (28, 28))
    return resized_cell.reshape(1, resized_cell.shape[0], resized_cell.shape[1], 1)

  @property
  def prediction(self):
    return self._prediction