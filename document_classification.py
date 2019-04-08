# -*- coding: utf-8 -*-
"""Predicting document class from given text."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import numpy as np
import nltk
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

__author__ = 'Devansh Jani <devanshjani@gmail.com>'

stemmer = PorterStemmer()
lammer = WordNetLemmatizer()
words = stopwords.words("english")


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


def predict_document_class(test_data: np.array):
    """
    Predict document class from model trained.

    :param test_data: Model validation using test data.
    """
    nltk.download('stopwords')
    training_data, target = read_training_data()
    training_data = [stemmer.stem(word) for word in training_data]
    training_data = [lammer.lemmatize(word) for word in training_data]
    target = list(map(int, target))
    pipeline = Pipeline([
        ('vec_idf', TfidfVectorizer(
            analyzer='char_wb',
            ngram_range=(1, 3),
            stop_words=words)),
        ('classifier', SGDClassifier(
            loss='hinge',
            penalty='l2',
            alpha=1e-3,
            n_iter=8,
            random_state=42)),
    ])
    pipeline.fit(training_data, target)

    for a_test in test_data:
        print(*pipeline.predict(a_test), sep='\n')


if __name__ == '__main__':
    """Predict document class."""
    no_of_test_data = int(input())
    testing_data = np.array(
        [input().split(sep=',') for _ in range(no_of_test_data)], str)
    predict_document_class(testing_data)
