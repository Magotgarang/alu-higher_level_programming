#/bin/bash
# Script that shows the content-length from a HTTP request
curl -sI "$" | grep "content-length:" |cut -d " " -f 2
