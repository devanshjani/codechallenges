# -*- coding: utf-8 -*-
"""Predicting dota games."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


def read_training_data() -> np.array:
    """
    Read training data for classifier training.

    :return: Numpy array for feature vector.
    """
    return np.loadtxt('dota_train.txt', delimiter=',', dtype='str')


def predict_dota_games(test_data: np.array):
    """
    Train decision tree classifier for dota games.

    :param test_data: Games to predict.
    """
    classifier = DecisionTreeClassifier()
    encoder = OneHotEncoder()
    traing_data = read_training_data()
    encoded_training_data = encoder.fit_transform(traing_data[:, :-1])
    encoded_test_data = encoder.transform(test_data)
    classifier.fit(encoded_training_data, traing_data[:, -1])
    prediction = classifier.predict(encoded_test_data)
    print(*prediction, sep='\n')


if __name__ == '__main__':
    """Predict dota games using tree classifier."""
    no_of_test_data = int(input())
    testing_data = np.array(
        [input().split(sep=',') for _ in range(no_of_test_data)], str)
    predict_dota_games(testing_data)
