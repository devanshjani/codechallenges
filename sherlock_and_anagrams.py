# -*- coding: utf-8 -*-
"""Sherlock and anagram solver using hash-maps."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link https://www.hackerrank.com/challenges/sherlock-and-anagrams

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


# Complete the sherlockAndAnagrams function below.

def sherlock_and_anagrams(anagram_string) -> int:
    """
    Calculate anagram pairs by given string.
    :param anagram_string: String for anagram validation
    :return: Number of anagram pairs.
    """
    collector = {}

    anagram_count = 0

    for i in range(len(anagram_string)):

        for j in range(i + 1, len(anagram_string) + 1):

            combination_str = list(anagram_string[i:j].strip())

            combination_str.sort()

            sorted_string = ''.join(combination_str)

            if sorted_string in collector:

                anagram_count += collector[sorted_string]

                collector[sorted_string] = collector[sorted_string] + 1

            else:
                collector[sorted_string] = 1

    return anagram_count


if __name__ == '__main__':
    print(sherlock_and_anagrams('dajshdeiirwahsgdhga'))
