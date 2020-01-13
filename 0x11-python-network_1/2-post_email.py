#!/usr/bin/python3
""" takes URL and email, sends POST request to passed URL
with email parameter, displays body response (decoded in utf-8)"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
        
