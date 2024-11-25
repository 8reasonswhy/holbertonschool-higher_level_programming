#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a class Square to represent a square shape.
"""


class Square:
    """
    Class representing a square with a private size attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method is a constructor that is called automatically
        when a new object is instantiated.
        Qaund on veut initialiser le truc python
        fait appel automatique au setter grace au tag
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour récupérer  valeur de size car elle est pri
        on est obliger d utiliser le tag  @property
        """
        return self.__size

    @property
    def position(self):
        """
        getter pour la position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter pour modifier la valeur de notre trucs privee il faut
        obligatoirement utiliser le tag @<nom de votre truc>.setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, position):
        """
        setter pour la position
        """
        if not (isinstance(position, tuple) and all(isinstance(x, int) and x > 0 for x in position) and len(position) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Méthode pour calculer l'aire du care
        """
        return self.__size ** 2

    def my_print(self):
        """
        la pour imprimer une image de notre carree on va dire
        """
        if self.size == 0:
            print('')
        else:
            for j in range(position[1]):
                print('')
            for i in range(self.size):
                print(' '*position[0] + '#'*self.size)
