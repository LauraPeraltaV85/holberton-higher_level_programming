#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0.5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    ques = {'q': q}
    r = requests.post(url, data=ques)
    try:
        r.raise_for_status()
        req = r.json()
        if len(req) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except ValueError:
        print("Not a valid JSON")
