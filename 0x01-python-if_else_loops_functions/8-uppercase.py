#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            m = ord(n) - 32
        else:
            m = ord(n)
        print("{:c}".format(m), end='')
    print()
