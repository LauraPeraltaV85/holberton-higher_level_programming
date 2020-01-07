#!/bin/bash
# sends a request, and displays the size of the body of the response
curl -sI $1 | grep "Content-Lenght" | cut -d " " -f2
