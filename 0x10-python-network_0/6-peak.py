#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """return the peak"""

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        temp = list_of_integers[0]
        return temp
