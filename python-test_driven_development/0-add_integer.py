#!/usr/bin/python3
def add_integer(a, b):
    """
    notre fonction qui fait l'ajout de deux entier
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not ( isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
