#!/usr/bin/python3
"""takes URL email sends post request to passed URL"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
