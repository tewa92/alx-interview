#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding
    """

    n = 0
    for num in data:
        mask = 1 << 7
        if n == 0:
            while mask & num:
                n += 1
                mask = mask >> 1
            if n == 0:
                continue
            if n == 1 or n > 4:
                return False
        else:
            if not (mask & num):
                return False
        n -= 1
    if n > 0:
        return False
    return True
