#!/usr/bin/python3
num = ", ".join([f"{i:02}" for i in range(1, 99) if int(f"{i:02}"[::-1]) > i])
print("{}".format(num))
