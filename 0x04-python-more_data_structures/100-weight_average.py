#!/usr/bin/python3
def weight_average(my_list=[]):
    z = 0
    y = 0
    if not my_list:
        return 0
    for x in my_list:
        z += (x[0] * x[1])
        y += x[1]
    return (z / y)
