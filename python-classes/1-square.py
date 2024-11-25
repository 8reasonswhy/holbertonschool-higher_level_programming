#!/usr/bin/python3
"""
Class squar avec un privat attribute size 
"""


class Square :
    """
    class Squar avec un attribue size private un attribue prive on lui ajout un double  _ devant lui pour dir que c'est priv√
    """


    def __init__(self,size):
        """ Alors la on d√©fini le constructeur appeler init sur python le constructeur est appele automatiquement 
        quand on veut instancier un nouveau object 
        """
        self.__size = size
