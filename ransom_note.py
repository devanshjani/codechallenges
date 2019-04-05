# -*- coding: utf-8 -*-
"""Ransom note solver using hash-maps."""
# Created: 2019-03-06 Devansh Jani <devansh.jani@mysinglesource.io>
# Challenge Link https://www.hackerrank.com/challenges/ctci-ransom-note

__author__ = 'Devansh Jani <devanshjani@gmail.com>'


from collections import Counter
from typing import List

"""
Validate the test cases below:
6 4
give me one grand today night
give one grand today

6 5
two times three is not four
two times two is four

7 4
ive got a lovely bunch of coconuts
ive got some coconuts
"""


def validate_ransom_note(
    magazine_words: List[str],
    ransom_note_words: List[str],
    magazine_words_entered: int,
    ransom_words_entered: int
) -> str:
    """
    Validate if ransom note can be constructed from the magazine string.
    :param magazine_words: List of strings for magazine words.
    :param ransom_note_words: List of ransom notes string.
    :param magazine_words_entered: Total words in magazine entered.
    :param ransom_words_entered: Total words in ransom note entered.
    :return: Yes, if ransom note can be created or No if not.
    """
    magazine_words = [
        word for word in magazine_words
        if isinstance(word, str) and len(word) >= 1 and not word.isdigit()]
    ransom_note_words = [
        word for word in ransom_note_words
        if isinstance(word, str) and len(word) <= 5 and not word.isdigit()]
    if (
        (Counter(ransom_note_words) - Counter(magazine_words)) == {} and
        len(magazine_words) >= 1 and
        len(ransom_note_words) <= 30000 and
        len(magazine_words) == magazine_words_entered and
        len(ransom_note_words) == ransom_words_entered
    ):
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    """Validate the ransom note construction from given magazine note."""

    word_counts = input().split()

    magazine_count = int(word_counts[0])

    ransom_count = int(word_counts[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(validate_ransom_note(magazine, note, magazine_count, ransom_count))
