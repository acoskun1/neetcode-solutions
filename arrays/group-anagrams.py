from typing import List
from collections import defaultdict
import unittest


class Solution:

    def __init__(self, strs: List[str]) -> None:
        self.strs = strs

    def groupAnagramsByFrequency(self) -> List[List[str]]:

        """
        Character frequency count to group anagrams.
        For each string creates a list "count" of size 26 - for each letter in the alphabet.
        List is then converted into a tuple to make it hashable - arrays cannot be keys in dict
        If the next string in the iteration matches a frequency in the hashmap, it is added to the array value.
        
        Time complexity: O(M.N) : M number of strings, N maximum length of a string.
        """

        ans = defaultdict(list)

        # iterates over each string. Runs M times where M = number of strings.
        for s in self.strs:
            count: List[int] = [0] * 26

            # iterates over each character to count frequencies. 
            # for each string takes O(N) time where N is length of the string.
            for c in s:
                count[ord(c) - ord("a")] += 1

            # takes O(26) time - list length is always fixed size. 
            ans[tuple(count)].append(s)
        
        return list(ans.values())

    def groupAnagramsBySorting(self) -> List[List[str]]:
    
        """
        Sorts characters of each string and converts to a tuple as the key to group anagrams
        
        Time Complexity: O(M,NlogN): M number of strings, N length of string
        """

        groups = defaultdict(list)
        for s in self.strs:
            groups[tuple(sorted(s))].append(s)

        return list(groups.values())



if __name__ == "__main__":
    sol = Solution(['eat','tea','ate','listen','silent','apple'])
    sol.groupAnagramsByFrequency()
    sol.groupAnagramsBySorting()
