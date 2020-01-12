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

  model = Sequential()
  model.add(Conv2D(32, kernel_size=(3, 3),
                  activation='relu',
                  input_shape=(X.shape[1],X.shape[2],1)))
  model.add(Conv2D(64, (3, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.25))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(num_classes, activation='softmax'))

  print(model.summary())

  print('Training Started...')


  model.compile(optimizer=Adadelta(),loss=categorical_crossentropy ,metrics=['accuracy'])
  model.fit(x=X, y=Y, epochs=epochs, validation_split=0.1)

  print('Training Finished...')

  print(model.evaluate(X, Y, verbose=1))

  model.save('./model/Model.h5')
  print('Model Saved in the directory...')