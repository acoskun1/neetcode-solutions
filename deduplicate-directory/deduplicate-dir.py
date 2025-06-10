"""
Given a directory, remove duplicate files.
"""
#!/usr/bin/env python3

import os
import sys
import hashlib
from typing import Optional

def hash_file(path: str, chunk_size: int = 8192) -> Optional[str]:
    """
    open file without loading the entire file to the memory - large file edge case
    hash chunks of the file instead of hashing the entire file content at once - large file edge case
    handle exceptions - permission, file does not exist
    """
    hash = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            while chunk:
                chunk = f.read(chunk_size)
                hash.update(chunk)
    except (FileNotFound, PermissionError):
        return None
    return hash.hexdigest()


def deduplicate_directory(path: str) -> None:
    """
    initialise a set to store unique hashes
    iterate the directory
    check if a symbolic link and not a regular file
    else, hash the file
    if hash exists remove file else add hash to set.
    """
    hash_set: set[str] = set()
    for root, dirs, filename in os.walk(path):
        for file in filename:
            file_path = os.path.join(root, file)
            if not os.path.isfile(file_path) or os.path.islink(file_path):
                continue
            file_hash = hash_file(file_path)
            if file_hash is None:
                continue
            if file_hash in hash_set:
                try:
                    os.remove(file_path)
                    print(f'Duplicate removed: {file_path}')
                except Exception as e:
                    print(f'Error removing: {e}')
            else:
                hash_set.add(file_hash)

if __name__ == "__main__":
    #usage python3 deduplicate-dir.py <path-to-dir>
    if len(sys.argv) != 2:
        print('Usage: ...')
        sys.exit(1)
    deduplicate_directory(sys.argv[1])
