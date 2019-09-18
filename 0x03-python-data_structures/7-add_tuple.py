#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = list(tuple_a)
    y = list(tuple_b)
    if len(x) < 2:
        for e in range(len(x), 2):
            x.append(0)
    if len(y) < 2:
        for e in range(len(y), 2):
            y.append(0)
    n = [x[0] + y[0], x[1] + y[1]]
    return (tuple(n))
