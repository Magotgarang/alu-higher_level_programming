#!/usr/bin/env python3
import sys

lines_read = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        try:
            ip, _, _, _, _, status, size = line.split()
            status = int(status)
            size = int(size)
            lines_read += 1
            total_size += size
            status_codes[status] += 1
        except ValueError:
            pass

        if lines_read % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print()

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
