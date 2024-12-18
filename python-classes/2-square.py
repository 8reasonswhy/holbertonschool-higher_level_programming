#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a class Square to represent a square shape.
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        """
        La méthode __init__ est un constructeurest  appelé automatiqueme POUR
        l'instanciation d'un nouvel objet
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
