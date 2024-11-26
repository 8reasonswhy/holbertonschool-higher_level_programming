#!/usr/bin/python3
"""
bon la fonction say my name 
"""
def say_my_name(first_name, last_name=""):
    """
    la fonction qui fait le trucs 
    """
    if not(isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif not(isinstance(las_name, str)):
        raise TypeError("last_name must be a string")
    print ("My name is", first_name, last_name)
