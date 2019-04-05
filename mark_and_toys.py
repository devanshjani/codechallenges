# -*- coding: utf-8 -*-
"""Mark and Toys solver using sor and search."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link https://www.hackerrank.com/challenges/mark-and-toys

__author__ = 'Devansh Jani <devanshjani@gmail.com>'

import itertools
import os
from typing import List


def mark_and_toys(prices: List, budget: int):
    """
    Compute max toys mark can buy.
    :param prices: tpy prices.
    :param budget: max budget.
    :return: No of toys that can be bought.
    """
    prices.sort()
    accumulated_prices = list(itertools.accumulate(prices))
    return next(
        agg_price[0]
        for agg_price in enumerate(
            accumulated_prices) if agg_price[1] > budget)


if __name__ == '__main__':
    # Set environ path before running. Stupid hacker-rank.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toys_and_budget = input().split()

    no_of_toys = int(toys_and_budget[0])

    toy_budget = int(toys_and_budget[1])

    toy_prices = list(map(int, input().rstrip().split()))

    result = mark_and_toys(toy_prices, toy_budget)

    fptr.write(str(result) + '\n')

    fptr.close()
