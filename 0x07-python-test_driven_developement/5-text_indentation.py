#!/usr/bin/python3
"""
    Prints text.
"""
def text_indentation(text):
    """Prints text with punctuation
    specifications, and specific 
    indentation.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 0
    while x < len(text):
        print("{:s}".format(text[x]), end="")
        if text[x] == '.' or text[x] == '?' or text[x] == ':':
            print()
            print()
            x += 1
        x +=1
