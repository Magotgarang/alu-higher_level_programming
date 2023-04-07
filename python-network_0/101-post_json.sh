#!/bin/bash
# comment
curl -sX POST -H "content-Type: application/json" -d @"$2" "$1"
