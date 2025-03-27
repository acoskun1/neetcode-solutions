from typing import List

"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.
"""

class Solution:

    def __init__(self, nums: List[int]) -> None:
        self.nums: List[int] = nums

    def longestConsecutiveHashMap(self) -> int:
        """
        Time Complexity and Space Complexity: O(N)
        
        * Setting up HashMap - O(N): iterates the array once.
        * Backward and Forward Searches - O(N): each number in the array is visited at most twice:
            Through one of the inner while loops
            Being the current num in the iteration

            After a num is processed in a while loop, it is marked true and not processed again in subsequent iterations. Each element is processed constant number of times regardless of array size. 
        """

        ans = 0
        hashNums = {num : False for num in self.nums}
        for num in self.nums:
            curr = 1
            nextel = num + 1
            while nextel in hashNums and not hashNums[nextel]:
                curr += 1
                hashNums[nextel] = True
                nextel +=1

            prev = num - 1
            while prev in hashNums and not hashNums[prev]:
                curr += 1
                hashNums[prev] = True
                prev -= 1

            ans = max(ans, curr)
        return ans

    def longestConsecutiveBruteForce(self) -> int:
        """
        Time Complexity & Space Complexity: O(N^2) 
        """
        
        if not self.nums: 
            return 0

        ans = 0
        for num in self.nums:
            curr_num = num
            curr_streak = 1

            while curr_num + 1 in self.nums:
                curr_num += 1
                curr_streak += 1

            ans = max(ans, curr_streak)

        return ans

    def longesConsecutiveSorting(self) -> int:
        """
        Time Complexity: O(n log N)
        Space Complexity: O(1)
        """
        
        if not self.nums:
            return 0

        self.nums.sort()
        ans = 1
        curr_streak = 1

        for i in range(1, len(self.nums)):
            if self.nums[i] == self.nums[i-1]:
                continue
            if self.nums[i] == self.nums[i-1] + 1:
                curr_streak += 1
            ans = max(ans, curr_streak)
            curr_streak +=1

        return max(ans, curr_streak)


if __name__ == "__main__":
    pass


