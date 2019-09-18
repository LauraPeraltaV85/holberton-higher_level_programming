#!/usr/bin/python3
def multiple_returns(sentence):
    s = len(sentence)
    for x in range(s):
        if s == 0:
            return None
        else:
            e = tuple([len(sentence), sentence[0]])
            return(e)
