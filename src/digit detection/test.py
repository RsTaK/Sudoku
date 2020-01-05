from keras.models import load_model

model = load_model('./model/mnist_digit_recognizer.h5')
print(model.summary())