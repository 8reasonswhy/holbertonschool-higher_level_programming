#!/usr/bin/python3
"""
Le programme qui fais les teste et nous fait l' addition des trucs 
"""


def add_integer(a, b):
    """
    notre fonction qui fait l'ajout de deux entier
    """
    if not (isinstance(a, (int, float)) or a is None):
        raise TypeError("a must be an integer")
    if not ( isinstance(b, (int, float)) or b is None):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
