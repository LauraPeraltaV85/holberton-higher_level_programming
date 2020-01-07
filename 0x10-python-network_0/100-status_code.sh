#!/bin/bash
# sends a request and displays only the status code of the response
curl -s -L -I -o -w "%{http_code}" $1
