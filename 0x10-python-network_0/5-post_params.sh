#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sL -X POST -H "email: hr@holbertonschool.com, subject: I will alwaysbe here for PLD" $1
