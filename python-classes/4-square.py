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
        Qaund on veut initialiser le truc pythin fait appel automatique au setter grace au tag
        """
        self.size = size  # Utilise le setter pour initialiser

    @property
    def size(self):
        """
        Getter pour récupérer  valeur de size car elle est prive 
        on est obliger d utiliser le tag  @property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour modifier la valeur de notre trucs privee il faut obligatoirement 
        utiliser le tag @<nom de votre truc>.setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Méthode pour calculer l'aire du carré (taille au carré).
        """
        return self.__size ** 2
