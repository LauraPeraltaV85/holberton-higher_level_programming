#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arr = dir(hidden_4)
    for n in arr:
        if n[0] != '_' and n[1] != '_':
            print("{}".format(n))
