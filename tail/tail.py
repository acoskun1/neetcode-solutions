#!/usr/bin/env python3 

import os
import sys
from typing import List

class Tail:

    def __init__(self, 
                 follow_lines: bool = False,
                 line_count: int = 10,
                 file_path: str
                 ) -> None:
        self.follow_lines = follow_lines
        self.line_count = line_count
        self.file_path = file_path
        self.regular_file = self._is_regular_file()

    def _is_regular_file(self) -> bool:
        if os.path.exists(self.file_path)
            and os.path.is_file(self.file_path)
            and not os.path.is_symlink(self.file_path)
            and not os.path.is_dir(self.file_path):
            return True
        else:
            return False

    def _get_n_lines(self, file) -> List[str]:
        """
        Helper method, reads the last n lines from a file. 
            n = self.line_count
        
        Seek to the end of file
        Read chunk backwards
        Accumulate lines
        Stop when enough lines are collected
        Handle edge cases
        """
        # Read last 'n' lines efficiently
        buffer = 1024 # Size (in bytes) of each chunk read from file.
        file.seek(0, os.SEEK_END) # Move file pointer to the end of the file.
        size = file.tell() # Get the current position == file size since we seeked the end...
        lines = [] # List to collect the lines read.
        pos = size # Keep track of current position while reading backwards. 
        while len(lines) < self.line_count and pos > 0: # Continue reading chunks backwards until we have enough lines, or reach start of file.
            read_size = min(buffer, pos) # Determine how many bytes to read next 
            pos -= read_size # Move current position back by chunk size.
            file.seek(pos) # Move file pointer to the new current position.
            chunk = file.read(read_size) # Read the chunk of data from the current position
            lines = chunk.splitlines(True) + lines # Split the chunk into lines keeping line endings and add them to front of the lines list.

        # Fallback for Small Files
        if len(lines) < self.line_count: # if file is too small, and not enough lines are collected, read the whole file, take the last n lines
            file.seek(0) # Reset the file pointer to the start aka. SEEK_SET
            lines = file.readlines()[-self.line_count:] # Read all lines and take the last n lines.
        
        # Return exactly n lines from the end of lines list.
        return lines[-self.line_count:] 

    def follow_file(self, file) -> str:
        """
        Helper method, continously reads last line of file and outputs to stdout.
        """
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            sys.stdout.write(line)
            sys.stdout.flush()


    def tail(self) -> None:
        if not self.regular_file:
            print(f"Error: {self.file_path} is not a regular file!")
            return
        try:
            with open(self.file_path, 'r') as file:
                for line in self._get_n_lines(file):
                    sys.stdout.write(line)
                sys.stdout.flush()

                if self.follow:
                    self.follow_file(file)
        except Exception as e:
            print(f'Error: {e}')


if __name__ == "__main__":
    # args
    follow_lines: bool = False
    line_count: int = 10
    file_path: str = None
    args = sys.argv[1:]

    i: int = 0
    while i < len(args):
        arg = args[i]
        if arg == "-f":
            follow_lines = True
        elif arg == '-n':
            i += 1
            line_count = int(args[i])
        else:
            file_path = arg

    if not file_path: sys.exit(1)

    tail = Tail(file_path, line_count, follow_lines)
    tail.tail()

