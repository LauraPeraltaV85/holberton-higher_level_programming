#!/usr/bin/python3
for n in range(0, 10):
    for n2 in range(0, 10):
        if n < n2:
            if n is 8 and n2 is 9:
                print("{}{}".format(n, n2))
            else:
                print("{}".format(n), end='')
                print("{},".format(n2), end=' ')
