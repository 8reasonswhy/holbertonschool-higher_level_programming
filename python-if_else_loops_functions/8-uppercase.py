#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            up += chr(ord(i)-32)
        else:
            up += i
    print("{}".format(up))
