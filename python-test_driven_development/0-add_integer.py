#!/usr/bin/python3
"""
Le programme qui fais les teste et nous fait l' addition des trucs 
"""
def add_integer(a, b):
    """
    notre fonction qui fait l'ajout de deux entier
    """
    if not (isinstance(a, (int, float)) and a is None):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not ( isinstance(b, (int, float)) and b is None):
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b

