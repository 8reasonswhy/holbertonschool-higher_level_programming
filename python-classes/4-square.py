#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a class Square to represent a square shape.
"""


class Square:
    """
    Class representing a square with a private size attribute.
    """
    def __init__(self, size=0):
        """
        The __init__ method is a constructor that is called automatically
        when a new object is instantiated.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This method returns the area of the square (size squared).
        """
        return self.__size ** 2
    
    def size(self, value):
        """
        la definition d un setter car l attribu est privee
        """
        self.__size = value
   
   def size(self):
       """
       on defini un getter car le truc est privee et pour acceder il nous faut un setter
       """
       return self.__size
~                                  
