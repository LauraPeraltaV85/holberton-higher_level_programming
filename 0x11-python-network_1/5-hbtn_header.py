#!/usr/bin/python3
"""takes URL, sends request URL displays value X-Request-Id"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
