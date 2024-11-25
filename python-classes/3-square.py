#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a class Square to represent a square shape.
"""


class Square:
    """
    Class square on defini la class avec le mot class 
    """
    def __init__(self, size=0):
        """
        la methode init est un constructeur appele automatiquement lors de 
        l instanciacion d un nouveau object 
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
     def area(self):
         """
         definition d un getter on va dire qui retourn l qire de carre
         """
        return self.__size**2
