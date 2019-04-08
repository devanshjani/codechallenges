# -*- coding: utf-8 -*-
"""Predicting home price regression problem."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


def predict_home_price(training: np.array, testing: np.array):
    """
    Predict house price for given data points from training.

    :param training: numpy array for polynomial fitting.
    :param testing: model evaluation.
    """
    polynomial_features = PolynomialFeatures(degree=3)
    regression_model = linear_model.LinearRegression()
    training_ = polynomial_features.fit_transform(training[:, :-1])
    testing_ = polynomial_features.fit_transform(testing)
    regression_model.fit(training_, training[:, -1])
    print(* regression_model.predict(testing_), sep='\n')


if __name__ == '__main__':
    """Predicting home prices by regression."""

    features, no_of_training_data = map(int, input().split())

    training_data = np.array(
        [input().split() for _ in range(no_of_training_data)], float)

    no_of_testing_data = int(input())

    testing_data = np.array(
        [input().split() for _ in range(no_of_testing_data)], float)

    predict_home_price(training_data, testing_data)
