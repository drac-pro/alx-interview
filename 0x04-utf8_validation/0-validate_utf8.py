#!/usr/bin/python3
"""defines a function validUTF8 for utf-8 validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    Args:
        data(list): list of integers
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        num = num & 0xFF
        if n_bytes == 0:
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 6:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
