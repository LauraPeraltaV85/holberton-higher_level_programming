#!/usr/bin/python3
def multiple_returns(sentence):
    s = len(sentence)
    if s == 0:
        x = None
    else:
        x = sentence[0]
    e = (s, x)
    return(e)
