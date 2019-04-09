# -*- coding: utf-8 -*-
"""Predicting document class from given text."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import nltk
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


def read_training_data() -> (List, List):
    """
    Read training data for classifier training.

    :return: Numpy array for feature vector.
    """
    target = []
    training_data = []

    with open('document_training.txt', 'rt') as training:
        no_of_samples = int(training.readline())
        for _ in range(1, no_of_samples):
            a_training = training.readline()
            training_data.append(a_training[1:])
            target.append(a_training[0])
    return training_data, target


def predict_document_class(validation_data: List[str]):
    """
    Predict document class from model trained.

    :param validation_data: Model validation using test data.
    """
    nltk.download('stopwords')

    data, target = read_training_data()
    target = list(map(int, target))

    (
        training_data,
        testing_data,
        training_target,
        testing_target) = train_test_split(
        data, target, test_size=0.33)

    tf_vec = TfidfVectorizer(
        sublinear_tf=True,
        norm='l2',
        encoding='latin-1',
        ngram_range=(1, 2),
        stop_words='english',
        max_features=10000
    ).fit(training_data)

    training_vec_data = tf_vec.transform(training_data)

    model = LinearSVC()
    model.fit(training_vec_data, training_target)

    predictions = model.predict(tf_vec.transform(testing_data))
    confusion_matrix(testing_target, predictions)  # Print this if needed
    validation_vec_data = tf_vec.transform(validation_data)

    for a_test in validation_vec_data:
        print(*model.predict(a_test), sep='\n')


if __name__ == '__main__':
    """Predict document class."""
    no_of_test_data = int(input())
    testing_data = [input() for _ in range(no_of_test_data)]
    predict_document_class(testing_data)
