#!/usr/bin/python3
"""
    Prints square.
"""
def print_square(size):
    """Prints square of hashtags"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    if size > 0:
        for count in range(size):
            for count in range(size):
                print('#', end='')
            print()
