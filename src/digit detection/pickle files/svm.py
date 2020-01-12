from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import pickle
from sklearn.model_selection  import train_test_split
import numpy as np

if __name__ == "__main__":

  pickle_out = open(r'src\digit detection\pickle files\X.pickle', 'rb')
  X = pickle.load(pickle_out)

  pickle_out = open(r'src\digit detection\pickle files\Y.pickle', 'rb')
  Y = pickle.load(pickle_out)

  (x, x_val, y, y_val) = train_test_split(X, Y,
	test_size=0.1, random_state=84)

  kVals = range(1, 30, 2)
  accuracies = []
  # loop over various values of `k` for the k-Nearest Neighbor classifier
  for k in range(1, 30, 2):
    # train the k-Nearest Neighbor classifier with the current value of `k`
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x, y)

    # evaluate the model and update the accuracies list
    score = model.score(x_val, y_val)
    print("k=%d, accuracy=%.2f%%" % (k, score * 100))
    accuracies.append(score)

  # find the value of k that has the largest accuracy
  i = int(np.argmax(accuracies))
  print("k=%d achieved highest accuracy of %.2f%% on validation data" % (kVals[i],
    accuracies[i] * 100))
  
  model = KNeighborsClassifier(n_neighbors=kVals[i])
  knnPickle = open('knnpickle_file', 'wb') 
  # source, destination 
  pickle.dump(model, knnPickle)  
  print('Model Saved in the directory...')