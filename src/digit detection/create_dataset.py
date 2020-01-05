import numpy as np
import cv2
import os
from random import shuffle
import pickle


if __name__ == "__main__":

  Data_dir = r'src\digit detection\data'
  Categories = os.listdir(Data_dir)
  IMG_SIZE = 28

  Training_Data = []

  for each_category in Categories:
    path = os.path.join(Data_dir, each_category)
    for each_img in os.listdir(path):
      try:
        img_array = cv2.imread(os.path.join(path, each_img))
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        Training_Data.append([img_array, int(each_category)])
      except Exception as e:
        pass
  
  print('Training Data loaded...')

shuffle(x=Training_Data)
X = []
Y = []

for features, labels in Training_Data:
  X.append(features)
  Y.append(labels)

print('Features and Labels generated...')
X = np.array(X).reshape((-1, IMG_SIZE, IMG_SIZE, 1))

pickle_out = open(r'src\digit detection\pickle files\X.pickle', 'wb')
pickle.dump(X, pickle_out)
pickle_out.close

pickle_out = open(r'src\digit detection\pickle files\Y.pickle', 'wb')
pickle.dump(Y, pickle_out)
pickle_out.close

print('Serialization completed...')
