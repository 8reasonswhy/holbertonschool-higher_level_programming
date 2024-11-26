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
    stop = False
    for l in text:
        if l =='.' or l == '?' or l == ':':
            print(l)
            print('')
            stop = True
        else:
            if stop:
                print(l.lstrip(), end='')
            else:
                print(l, end ='')
