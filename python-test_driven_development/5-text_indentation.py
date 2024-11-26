#!/usr/bin/python3
"""
la fonction qui saute la line
"""
def text_indentation(text):
    """
    le coeur de notre fonction 
    """
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    for l in text:
        if l =='.' or l == '?' or l == ':':
            print(l)
            print('')
        else:
            print(l, end = '\n')
