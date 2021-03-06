import time
import arff
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit
from utilities.plot_learning_curve import plot_learning_curve

start_time = time.perf_counter()

print("Importing dataset: FCSIT 2018 Phishing Examples")

dataset = arff.load(open('dataset_FCSIT_2018.arff', 'rt'))
data = np.array(dataset['data'])

print("Number of data points: ", data.shape[0])
print("Number of features: ", data.shape[1] - 1)

X = data[:, 0:48]
y = data[:, 48:49]

n_estimators = 7
max_depth = 11

print("Training the model with Random Forest")
estimator = RandomForestClassifier(criterion='entropy', n_jobs=-1, n_estimators=n_estimators, max_depth=max_depth)

cv = ShuffleSplit(n_splits=30, test_size=0.2, random_state=0)

plt = plot_learning_curve(estimator, "Learning Curves (Random Forest | estimators = " + str(
    n_estimators) + ", " + "max depth = " + str(max_depth) + ")", X, np.ravel(y, order='C'),
                          ylim=(0.8, 1.01), cv=cv, n_jobs=-1)
plt.show()
print('Time took:', time.perf_counter() - start_time, "seconds")
