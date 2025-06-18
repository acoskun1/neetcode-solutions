#!/usr/bin/env python3 

import os
import sys
from typing import List

class Tail:

    def __init__(self, file_path: str, follow: bool = False, line_count: int = 10) -> None:
        """
        follow:     bool: '-f' option, continuously prints end of file
        file_path:  str : path of file
        line_count: int : number of lines to print from the end
        
        is_regular_file: bool: regular file 
        """
        self.follow = follow
        self.line_count = line_count
        self.file_path = file_path 
        self.is_regular_file = self._is_regular_file()

    def _is_regular_file(self) -> bool:
        """
        Checks if file_path exists, valid file, not a symbolic link and not a directory
        """
        if (os.path.exists(self.file_path)
                and os.path.isfile(self.file_path) 
                and not os.path.islink(self.file_path) 
                and not os.path.isdir(self.file_path)):
            return True
        return False

    def tail(self) -> None:
        """
        Entrypoint, if file is valid and accessible, it prints "n" lines using
        _get_n_lines helper method which returns a list of lines.

        If following, uses follow_lines helper method which constantly prints last line.
        """
        if not self.is_regular_file:
            print(f"{self.file_path} is not a valid file!")
            return
        try:
            with open(self.file_path, 'r') as file:
                for line in self._get_n_lines(file):
                    if line:
                        print(f'{line}\n')

                if self.follow:
                    self.follow_lines(file)
        except Exception as e:
            print(f'Error: {e}')

    def _get_n_lines(self, file) -> List[str]:
        """
        Helper method, reads a file backwards in chunks and returns a list of lines.

        lines:  list of lines
        pos:    current file pointer - gets updated as chunks are read backwards
        buffer: size in bytes of each chunk read from file (1 KiB)
        """
        lines: List[str] = []
        file.seek(0, os.SEEK_END) # Move file pointer to the end of the file.
        pos = file.tell() # Tracks current file pointer position while reading backwards.
        buffer: int = 1024 #1KiB
        while len(lines) < self.line_count and pos > 0: #until enough lines are collected and file pointer comes to start of file.
            read_size = min(buffer, pos) # if pos < 1KiB read only pos amount, no need to read excess bytes. Fallback.
            pos -= read_size # after each read, push pos back by read_size.
            chunk = file.read(read_size) # read chunk
            lines = chunk.splitlines() + lines # collect lines by splitting and adding new lines to front of the list.

        #if after reading backwards, the number of lines collected is less than required,
        #adjust file pointer to beginning of the file and read all lines and only return n many from the end.
        if len(lines) < self.line_count:
            file.seek(0)
            lines = file.readlines()[-self.line_count:]

        #return n many lines starting from the back == latest line.
        return lines[-self.line_count:]

    def follow_lines(self, file) -> None:
        """
        Helper method, continuously prints the last line. Sends file pointer to the end of file and 
        reads that line at the position. Repeats constantly
        """
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            print(f'{line}\n')

if __name__ == "__main__":
    args = sys.argv[1:]
    line_count = 10 
    follow = False
    file_path = None

    i = 0 
    while i < len(args):
        arg = args[i]
        if arg == "-n":
            i += 1 
            line_count = int(args[i])
        elif arg == '-f':
            follow = True
        else:
            file_path = arg
        i += 1

    tail = Tail(file_path, follow, line_count)
    tail.tail()
