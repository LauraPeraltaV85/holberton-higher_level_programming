#!/bin/bash
# sends a GET request to the URL, and 
# displays the body of the response
curl -Ls -X -G "$1"
