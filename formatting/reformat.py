"""
Given a directory rename .yaml files to .yml
"""
#!/usr/bin/env python3

import os
import sys

"""
Scan the directory which should return an iterator - os.scandir(path='.')
Iterate each object name and check if it endswith .yaml
If endswith .yaml, create new file name and new_path which should consist of path + new_name
Check if new file name already exists in the path, then skip. Else: rename file - os.rename
Handle exception, OSError, for file permission errors and file in use etc.
"""

def reformat_yaml_files(path: str) -> None:
    #scan the directory which returns an iterator.
    for obj in os.scandir(path):
        #if it is a file (not a symbolic link) and ends with .yaml create new file name and path.
        extension = obj.name.split('.')[-1]
        if obj.is_file() and extension == 'yaml':
            new_name = obj.name[:-5] + '.yml'
            new_path = os.path.join(path, new_name)
            #check if the new file already exists in the path, if so skip
            try:
                if os.path.exists(new_path):
                    print(f'Skipping {obj.name}, {new_path} already exists!')
                    continue
                #if new file does not exist in the path, rename the file.
                os.rename(obj.path, new_path)
                print(f'Renamed: {obj.name} -> {new_name}')
            except (OSError, PermissionError, FileNotFoundError) as e:
                print(f'Error renaming {obj.name}: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ...')
        sys.exit(1)
    reformat_yaml_files(sys.argv[1])
