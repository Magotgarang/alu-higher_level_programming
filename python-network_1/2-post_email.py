#!/usr/bin/bash
"""documented"""

import urllib.request
import urllib.parse
import sys

if --name-- == ' --main--':
"""Documented"""
url = sys.argv[1]
valuesl = {"email":sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
content = response.read()
print("{}".format(content.decode("utf-8")))
