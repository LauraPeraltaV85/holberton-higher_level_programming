#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 is 0:
        m = chr(n)
    else:
        m = chr(n - 32)
    print("{}".format(m), end='')
