#!/usr/bin/python3
def multiple_returns(sentence):
    s = len(sentence)
    if s is None:
        return None
    else:
        e = (s, sentence[0])
        return(e)
