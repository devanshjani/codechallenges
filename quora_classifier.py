# -*- coding: utf-8 -*-
"""Predicting quora answers."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/quora-answer-classifier/problem

import re
import warnings
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings('ignore')

if __name__ == '__main__':
    """Predicting quora answers."""
    # Training data manipulations.
    no_of_train, features = map(int, input().split())
    data = [input() for _ in range(no_of_train)]
    train_data = [a_target[9:] for a_target in data]
    train_target = list(map(int, [a_target[6:8] for a_target in data]))
    # Testing data manipulations.
    no_of_test = int(input())
    data = [input() for _ in range(no_of_test)]

    test_data = [a_target[6:] for a_target in data]
    test_id = [a_target[:5] for a_target in data]

    train_data_dict = [
        {k: v.strip('"') for k, v in re.findall(r'(\S+):(".*?"|\S+)', line)}
        for line in train_data]

    test_data_dict = [
        {k: v.strip('"') for k, v in re.findall(r'(\S+):(".*?"|\S+)', line)}
        for line in test_data]

    training_matrix = DataFrame(train_data_dict).values
    testing_matrix = DataFrame(test_data_dict).values

    quora_classifier = RandomForestClassifier()

    quora_classifier.fit(training_matrix, train_target)

    prediction = quora_classifier.predict(testing_matrix).tolist()

    for a_test, a_prediction in zip(test_id, prediction):
        print(a_test, '+1' if a_prediction == 1 else '-1')
