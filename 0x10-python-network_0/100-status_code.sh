#!/bin/bash
# sends a request and displays only the status code of the response
curl -sL -I -o /dev/null -w "%{http_code}" $1
