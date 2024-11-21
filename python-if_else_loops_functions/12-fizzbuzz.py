#!/usr/bin/python3
def fizzbuzz():
    rt = ""
    for i in range (1, 101):
        if i % 3 == 0:
            rt += "Fizz"
            if i % 5 == 0:
                rt += "Buzz "
            else:
                rt += " "
        elif i % 5 ==0:
            rt += "Buzz "
        else:
            rt += str(i)+" "
    print(rt, end="")
