#!/usr/bin/env python3

"""
Given a text file count most repeated words, list them, sort, and show number of repeatings.

Approach:

    strip and split text
    chunk read without loading entire text file to memory
    count words into hashmap
    bucket sort
"""
import sys
from collections import defaultdict

def word_count(file: str, chunk_size: int, k: int = 0) -> dict:
    word_map = defaultdict(int)

    with open(file, 'r') as text:
        while True:
            chunk = text.read(chunk_size)
            if not chunk:
                break

            for word in chunk.lower().split():
                if word:
                    word_map[word] = word_map.get(word, 0) + 1

    max_count = max(word_map.values(), 0)
    freq = [[] for _ in range(max_count + 1)]
    for word, count in word_map.items():
        freq[count].append(word)

    """
    if asked top k frequent:

    ans = []
    for i in range(len(nums), 0, -1):
        for value in freq[i]:
            ans.append(value)
            if len(ans) == k:
                return ans
    """

    return freq[-1].sort()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: --')
        sys.exit(1)
    ans = word_count(sys.argv[1])
