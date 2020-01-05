import os
import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

df = pd.read_csv(r'src\digit detection\data\dataset.csv')
df_x = np.array(df.iloc[:,0:1])
df_y = np.array(df.iloc[:,1:2])

onehot_encoded = to_categorical(df_y)

X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=42, stratify = df_y, shuffle = True)

X_test = to_categorical(y_train)
y_test = to_categorical(y_test)
 

img = cv2.imread(X_train.item(0))

img = cv2.resize(img,(64, 64))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 9, 17, 17)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,4)

thresh = thresh.astype(np.float32)
thresh/=255

cv2.imshow('A',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()