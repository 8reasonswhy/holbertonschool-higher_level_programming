#!/usr/bin/python3
num = ", ".join([f"{i:02}" for i in range(1, 99) if int(str(i)[::-1]) > i])
print("{}".format(num))
