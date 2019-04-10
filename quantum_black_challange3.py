# -*- coding: utf-8 -*-
"""Challenge 3: ."""
# Created: 2019-04-10 Devansh Jani <devanshjani@gmail.com>
import numpy as np
from numpy import genfromtxt
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier


def train_classifier(train_data: np.array, target: np.array, test: np.array):
    """
    Train image classifier for given images.
    :param train_data: image data.
    :param target: Multi-class labels.
    :param test: Testing data.
    """
    # Doing some parameter tuning, possibly can do cross validation
    # Sampling and grid search given more time than 10 sec to converge.
    rf_clf = RandomForestClassifier(max_depth=50, n_estimators=100)

    image_cls = OneVsRestClassifier(rf_clf)

    image_cls.fit(train_data, target)

    prediction = image_cls.predict(test)
    # Casting int for prediction numpy array.
    prediction = prediction.astype(int)
    # Saving csv for predictions.
    np.savetxt('prediction.csv', prediction, delimiter=',', fmt='%i')


if __name__ == '__main__':
    """Classifying processed images."""

    # Storing this in feature vector array.

    training_data_with_target = genfromtxt('train.csv', delimiter=',')
    test_data = genfromtxt('test.csv', delimiter=',')

    # Just data
    training_data: np.array = training_data_with_target[:, :-6]

    # Just targets.
    training_target: np.array = training_data_with_target[:, -6:]

    # Training Decision tree classifier.
    train_classifier(training_data, training_target, test_data)
