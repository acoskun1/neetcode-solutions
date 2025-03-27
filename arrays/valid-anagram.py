import typing
import unittest

"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:

    def __init__(self, s: str, t: str) -> None:
        self.s: str = s
        self.t: str = t

    # O(1) solution
    def isAnagramSorted(self) -> bool:
        return sorted(self.s) == sorted(self.t)

    # O(n) solution
    def isAnagram(self) -> bool:

        #anagrams must have the same length
        if len(self.s) != len(self.t):
            return False

        #create two separate hashmaps that stores the character counts of each string
        mapS, mapT = dict(), dict()

        #create an iteration that counts the frequency of each character
        for i in range(0, len(self.s)):
            mapS[self.s[i]] = mapS.get(self.s[i], 0) + 1
            mapT[self.t[i]] = mapT.get(self.t[i], 0) + 1

        #return true if the frequencies of all characters are matching
        for j in mapS:
            if mapS[j] != mapT.get(j, 0):
                return False
        return True

class TestSolution(unittest.TestCase):

    def test_empty_strings(self):
        sol = Solution("", "")
        self.assertTrue(sol.isAnagram())
        self.assertTrue(sol.isAnagramSorted())

    def test_identical_strings(self):
        sol = Solution("listen", "listen")
        self.assertTrue(sol.isAnagram())
        self.assertTrue(sol.isAnagramSorted())

    def test_anagrams(self):
        sol = Solution("listen", "silent")
        self.assertTrue(sol.isAnagram())
        self.assertTrue(sol.isAnagramSorted())

    def test_not_anagrams_different_lengths(self):
        sol = Solution("abc", "ab")
        self.assertFalse(sol.isAnagram())
        self.assertFalse(sol.isAnagramSorted())

    def test_not_anagrams_different_characters(self):
        sol = Solution("hello", "world")
        self.assertFalse(sol.isAnagram())
        self.assertFalse(sol.isAnagramSorted())

    def test_anagrams_with_different_character_counts(self):
        sol = Solution("aabbcc", "abcabc")
        self.assertTrue(sol.isAnagram())
        self.assertTrue(sol.isAnagramSorted())

if __name__ == "__main__":
    unittest.main()


