from typing import List
import unittest




# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:

    def __init__(self, nums: List[int]) -> None:
        self.nums: List[int] = nums

    def hasDuplicate(self) -> bool:
        
        seen: set[int] = set()
    
        for i in self.nums:
            if i in seen:
                return True
            seen.add(i)
        return False

class TestSolution(unittest.TestCase):
    
    def test_no_duplicates(self):
        sol = Solution([1,2,3,4,5])
        self.assertFalse(sol.hasDuplicate())

    def test_has_duplicates(self):
        sol = Solution([1,2,2,3,4,5,6])
        self.assertTrue(sol.hasDuplicate())

    def test_empty_list(self):
        sol = Solution([])
        self.assertFalse(sol.hasDuplicate())

    def test_single_element(self):
        sol = Solution([1])
        self.assertFalse(sol.hasDuplicate())

    def test_all_elements_same(self):
        sol = Solution([1, 1, 1, 1])
        self.assertTrue(sol.hasDuplicate())

    def test_large_list_with_duplicates(self):
        sol = Solution(list(range(10000)) + [5000])
        self.assertTrue(sol.hasDuplicate())

    def test_large_list_without_duplicates(self):
        sol = Solution(list(range(10000)))
        self.assertFalse(sol.hasDuplicate())

    def test_multiple_duplicates(self):
        sol = Solution([1, 2, 3, 1, 4, 5, 2])
        self.assertTrue(sol.hasDuplicate())

    def test_no_duplicates_in_large_list(self):
        sol = Solution([i for i in range(100000)])
        self.assertFalse(sol.hasDuplicate())

    def test_duplicates_at_start_and_end(self):
        sol = Solution([1, 2, 3, 4, 5, 1])
        self.assertTrue(sol.hasDuplicate())


if __name__ == "__main__":
    unittest.main()
