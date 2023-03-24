#!/usr/bin/env python3

import sys

# initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # loop through standard input
    for line in sys.stdin:
        # increment line count
        line_count += 1
        
        # parse line
        parts = line.split()
        status_code = int(parts[8])
        file_size = int(parts[9])
        
        # update metrics
        total_size += file_size
        status_codes[status_code] += 1
        
        # check if 10 lines have been processed
        if line_count % 10 == 0:
            # print statistics
            print("Total file size: File size:", total_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
            print()
        
except KeyboardInterrupt:
    # print final statistics on keyboard interruption
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
