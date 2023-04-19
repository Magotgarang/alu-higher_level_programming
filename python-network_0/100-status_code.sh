#!/bin/bash
# a Bash script that sends a resquest to a URL passed as an argument, and display only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
