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

Format:

    $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
"""

#!/usr/bin/python3

import os
import time

#define the log file location
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
            #log_line is an iterator which can be iterated - each iteration will be a line collected at tail
            log_line = follow_lines(f)
            for line in log_line:
                #split the string into a list of strings separated by whitespace
                parts = line.split()
                if len(parts) < 9:
                    continue
                #set variables according to parts[] indexing - print(parts)
                ip_address = parts[0]
                http_response_code = parts[8]
                #request detail is enclosed inside double quotes of each log entry.
                req_start = line.find('"') #finds the first double quote
                req_end = line.find('"', req_start + 1) #finds the closing quote for setting request boundaries.
                if req_start == -1 or req_end == -1:
                    continue
                request = line[req_start+1: req_end]
                if http_response_code != '200':
                    print(f'{ip_address} - {request} - {http_response_code}')

    except KeyboardInterrupt:
        print("\nKeyboardInterrupted. Stopped Monitoring")
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
