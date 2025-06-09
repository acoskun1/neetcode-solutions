
#!/usr/bin/env python3

import os
import sys
import hashlib
from typing import Optional

def deduplicate_directory(path: str) -> None:
    #initialise a set to store unique hashes
    seen_hash: set[str] = set()

    #iterate each file, hash it and check if it exists in seen_hash
    for dirpath, dirname, filename in os.walk(path):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            if not os.path.isfile(filepath) or os.path.islink(filepath):
                continue
            filehash = hash_file(filepath)
            if filehash is None:
                continue
            if filehash in seen_hash:
                try:
                    os.remove(filepath)
                    print(f"Removed duplicate file: {filepath}")
                except Exception as e:
                    print(f'Error removing {filepath}: {e}')

            else:
                seen_hash.add(filehash)

def hash_file(path: str, chunk_size: int = 8192) -> Optional[str]:
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
    except (PermissionError, FileNotFoundError):
        return None
    return hasher.hexdigest()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 deduplicate-dir.py <path-to-directory>')
        sys.exit(1)
    else:
        deduplicate_directory(sys.argv[1])
