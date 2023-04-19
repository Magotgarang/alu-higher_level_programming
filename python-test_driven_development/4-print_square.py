#!/usr/bin/python3
"""A function that prints a square with the character # ."""


def print_square(size):
    """print a square with the # character.
    Args:
    size (int): The height/width of the sqaure.
    Raise:
    TypeError: if size is not an integer.
    ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0"

                for i in range(size):
                [print("#"' end="") for j in range(size)]
                print("")
