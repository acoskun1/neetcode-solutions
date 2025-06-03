"""
Given a file /var/log/nginx/access.log write a python script that outputs nginx
logs with response code other than 200 on user console.

Script should continuously monitor the file until interrupt signal is invoked.
Output should be in the following format:

    f'{ip_address}: {http_response_code}: {access_path}'
---
Suggestions:

Make the script memory efficient by avoiding loading the entire file to the memory.
Parse the bottom line of the file then apply the logic.
---
Assumptions:

A log entry will be written to the access.log file per second.
Each log entry will have identical formatting.
"""

#!/usr/bin/python3

import os
import time

log_file: str = '/var/log/nginx/access.log'

def follow_lines(file) -> str:
    #get the tail of the file by changing stream position to end of file
    file.seek(0, os.SEEK_END)
    #continuously read the last line starting from the tail as new entries are made to access.log
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def main() -> None:
    try:
        #without loading the entire file to the memory, get tail of file
        with open(log_file, 'r') as f:
            log_line: str = follow_lines(f)
            #parse the log entry into a hashmap {'ip_address':'IP_ADDRESS', 'http_response': 'HTTP response'} etc
            

    except KeyboardInterrupt:
        print('n\KeyboardInterrupted. Stopped Monitoring')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
