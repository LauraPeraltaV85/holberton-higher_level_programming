#!/usr/bin/python3
"""takes URL sends request to URL displays
body of response (decoded in utf-8)"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys
    try:
        with urlib.request.urlopen(sys.argv[1]) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
