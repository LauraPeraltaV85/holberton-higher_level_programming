#!/usr/bin/python3
"""takes URL, sends request to URL and displays value
of X-Request-Idfound in header of response"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
