# -*- coding: utf-8 -*-
"""Mark and Toys solver using sort and search."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import os
from statistics import median
from collections import deque
from typing import List

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


# Complete the activityNotifications function below.
def activity_notifications(expenditure: List[int], no_of_days: int) -> int:
    """
    Calculate fraudulent notification counts.

    :param expenditure: Expenditure data for fraudulent activity counts.
    :param no_of_days: Median window for fraud activity count.
    :return: Fraud notification counts.
    """
    median_data = deque(expenditure[:no_of_days])
    spending_data = deque(expenditure[no_of_days:])
    median_spending = median(median_data)
    no_of_reports = 0
    while spending_data:
        spend = spending_data.popleft()
        if spend >= median_spending * 2:
            no_of_reports += 1
        median_data.popleft()
        median_data.append(spend)
        median_spending = median(median_data)
    return no_of_reports


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    spending_and_days = input().split()

    days = int(spending_and_days[0])

    median_window = int(spending_and_days[1])

    spending = list(map(int, input().rstrip().split()))

    result = activity_notifications(spending, median_window)

    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
