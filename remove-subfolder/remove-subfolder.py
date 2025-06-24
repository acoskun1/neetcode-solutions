#!/usr/bin/env python3

from typing import List

"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
"""

class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.end: bool = False

    def insert(self, path):
        curr = self
        for folder in path.split("/"):
            if folder not in curr.children:
                curr.children[folder] = Trie()
            curr = curr.children[folder]
        curr.end = True

    def prefix_search(self, path) -> bool:
        curr = self
        folders = path.split("/")
        for i in range(len(folders) -1):
            curr = curr.children[folders[i]]
            if curr.end:
                return True
        return False

    def remove_sub_folders(self, folders: List[str]) -> List[str]:
        res: List[str] = []
        for folder in folders:
            trie.insert(folder)

        for folder in folders:
            if not self.prefix_search(folder):
                res.append(folder)

        return res



if __name__ == '__main__':
    folders: List[str] = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    trie = Trie()
    ans = trie.remove_sub_folders(folders)
    print(ans)

