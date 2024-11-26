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
        if l in ['.','?',':']:
            print(l)
            print()
            stop = True
        else:
            if stop:
                if l == ' ':
                    pass
                else:
                    print(l.lstrip(), end='')
                    stop = False
            else:
                print(l, end ='')
