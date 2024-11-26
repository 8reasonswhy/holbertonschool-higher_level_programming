#!/usr/bin/python3
"""
la fonction qui saute la line
"""


def text_indentation(text):
    """
    le coeur de notre fonction
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    stop = False
    for tt in text:
        if tt in ['.', '?', ':']:
            print(tt)
            print()
            stop = True
        else:
            if stop:
                if tt == ' ':
                    pass
                else:
                    print(tt.lstrip(), end= '')
                    stop = False
            else:
                print(tt, end = '')
