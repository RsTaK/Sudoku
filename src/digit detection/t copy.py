import pickle
from keras.optimizers import Adadelta
from keras.losses import categorical_crossentropy
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, Activation

if __name__ == "__main__":

  pickle_out = open(r'src\digit detection\pickle files\X.pickle', 'rb')
  X = pickle.load(pickle_out)

  pickle_out = open(r'src\digit detection\pickle files\Y.pickle', 'rb')
  Y = pickle.load(pickle_out)

  num_classes = 10
  epochs = 12

  Y = to_categorical(Y, num_classes)

  X = X/255.0

    
  #build the model
  model = Sequential()
  #add convolutional layers with input that matches our dataset
  model.add(Conv2D(254, kernel_size=(3,3), input_shape=(28,28, 1)))
  model.add(MaxPooling2D((2,2)))
  model.add(Conv2D(128, kernel_size=(3,3)))
  model.add(MaxPooling2D((2,2)))
  #convert from 2D input to 1D vectors
  model.add(Flatten())
  #finish our model with densely connected layers
  model.add(Dense(140, activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(80, activation='relu'))
  model.add(Dropout(0.2))
  #output layer with 10 units (one per each class 0-9)
  model.add(Dense(units=10, activation='sigmoid'))

  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

  model.fit(x=X, y=Y, epochs=epochs, validation_split=0.1)

  print('Training Finished...')

  print(model.evaluate(X, Y))

  model.save('./model/Model.h5')
  print('Model Saved in the directory...')