#!/usr/bin/env python3

"""
Given a text file count most repeated words, list them, sort, and show number of repeatings.
"""
import sys
from collections import defaultdict

def word_count(file: str) -> dict:
    word_map = defaultdict(int)
    with open(file, 'r') as text:

    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: --')
        sys.exit(1)
    ans = word_count(sys.argv[1])
