import unittest 

class Solution:
    
    def __init__(self, s: str) -> None:
        self.string = s


    def lenOfLongestSubstring(self) -> int:

        """
        res:        int -   length of longest substring
        char_set:   set -   set holding unique characters in sliding window.
        l, r:       int -   left and right boundaries of a sliding window.

        As the window expands, substring is valid if s[r] is not in char_set. Add s[r] into char_set.

        If s[r] is in char_set, an invalid substring is formed in the current window. Contract the window
        starting from the left until repeated char is no longer in the window/charset.
        Then add s[r] into char_set again. 

        Find the length of current valid window after contracting the window.

        eg: s = abcdbcdd

                a   b   c   d   b   c   d   d
                L               R                     - substring in this window LR is invalid
                                                        set: (a, b, c, d)
                                                        length: 4

                contract window until s[R] is no longer in the set starting from s[L]

                a   b   c   d   b   c   d   d           set: (c, d)
                        L       R                   

                since s[R] not in charset anymore, add it to charset and find length of current valid window
                length = right - left + 1 (+1 because you want to include current position of R too.)
                eg: r,l = 4,2 -> then r-l = 2 but actual length is 3.
        """
        
        res: int = 0
        char_set = set()
        l = 0

        for r in range(len(self.string)):
            #remove chars until s[r] is no longer in set.
            while self.string[r] in char_set:
                char_set.remove(self.string[l])
                l += 1
            char_set.add(self.string[r])
            length = r - l + 1
            res = max(res, length)
        return res

class TestSolution(unittest.TestCase):
    
    def test_empty_string(self):
        sol = Solution('')
        test = sol.lenOfLongestSubstring()
        self.assertEqual(test, 0, f'Invalid substring length {test}')

    def test_singlechar_repetitive_string(self):
        sol = Solution('eeeeeeeeeee')
        test = sol.lenOfLongestSubstring()
        self.assertEqual(test, 1, f'Invalid substring length {test}')

    def test_valid_substring(self):
        sol = Solution('abcabcbb')
        test = sol.lenOfLongestSubstring()
        self.assertEqual(test, 3, f'Invalid substring length {test}')

    def test_valid_substring_1(self):
        sol = Solution('abcdbcdd')
        test = sol.lenOfLongestSubstring()
        self.assertEqual(test, 4, f'Invalid substring length {test}')

if __name__ == '__main__':
    unittest.main()
