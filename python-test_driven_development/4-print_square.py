#!/usr/bin/python3
"""
la fonction qui dessice le truc
"""
def print_square(size):
    """
    la fonction qui fait les trucs
    """
    if not(isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0 :
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#"*size)
