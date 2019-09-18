#!/usr/bin/python3
def multiple_returns(sentence):
    for x in range(len(sentence)):
        if sentence is None:
            sentence[0] = None
        else:
            e = tuple([len(sentence), sentence[0]])
            return(e)
