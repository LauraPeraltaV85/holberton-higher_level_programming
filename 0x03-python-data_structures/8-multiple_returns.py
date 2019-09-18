#!/usr/bin/python3
def multiple_returns(sentence):
    s = len(sentence)
    if s == 0:
        sentence[0] = None
    else:
        e = (s, sentence[0])
    return(e)
