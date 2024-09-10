from typing import List
import typing
import unittest

"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

class Solution:

    def __init__(self, nums: List[int], target: int) -> None:
        self.nums: List[int] = nums
        self.target: int = target
    
    def twoSum(self) -> List[int]:
        # Create a hashmap that stores the index number against the remainder after item is subtracted
        numsH = dict()
        for index, value in enumerate(self.nums):
            diff = self.target - value
            if diff in numsH:
                return [numsH[diff], index]
            numsH[value] = index

class TestSolution(unittest.TestCase):

    def test_example_case_1(self):
        sol = Solution([2, 7, 11, 15], 9)
        self.assertEqual(sol.twoSum(), [0, 1])

    def test_example_case_2(self):
        sol = Solution([3, 2, 4], 6)
        self.assertEqual(sol.twoSum(), [1, 2])

    def test_example_case_3(self):
        sol = Solution([3, 3], 6)
        self.assertEqual(sol.twoSum(), [0, 1])

    def test_negative_numbers(self):
        sol = Solution([-1, -2, -3, -4, -5], -8)
        self.assertEqual(sol.twoSum(), [2, 4])

    def test_target_zero(self):
        sol = Solution([0, 4, 3, 0], 0)
        self.assertEqual(sol.twoSum(), [0, 3])

if __name__ == "__main__":
    unittest.main()

