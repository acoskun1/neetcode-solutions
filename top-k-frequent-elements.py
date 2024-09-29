from typing import List
from heapq import heapify, heappop

"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

"""

class Solution:

    def __init__(self, nums: List[int], k: int) -> None:
        self.nums = nums
        self.k = k

    #O(N) linear time complexity and space complexity.
    def topKFrequentBucketSort(self) -> List[int]:
        
        #create a hashmap that stores the count of each element
        #O(N) operation: n = number of elements in nums.
        count = {}
        for num in self.nums:
            count[num] = count.get(num, 0) + 1
        
        #create an array that stores index number as the occurrence and the element at that index as the values that occurr index times.
        #example: index 2 is for elements that occur twice.
        frq = [[] for i in range(len(self.nums) + 1)] #creates array that has len(nums)+1 many sub arrays.
        #O(N): n = number of distinct elements in count hashmap.
        for num, count in count.items(): #puts each item in the count hashmap, to its corresponding index, considering index == the occurrence of each item. 
            frq[count].append(num)

        #right most index of frq array is highest occurrence.
        # starting from the right, if the rightmost index has a value, add it to the result array.
        # result array holds the top k frequent elements.
        # if the length of result array == k, return res.
        # O(N): n = size of the frq array. Traverses the fixed size array which is == len(nums)+1 and adds only k elements. 
        res: List[int] = []
        for i in range(len(frq) - 1, 0, -1):
            for n in frq[i]:
                res.append(n)
                if len(res) == self.k:
                    return res

    def topKFrequentMinHeap(self) -> List[int]:
        count = {}
        arr = []
        for num in self.nums:
            count[num] = count.get(num, 0) + 1

        for num, count in count.items():
            arr.append((-count, num))

        heapify(arr)
        res = []
        while len(res) < self.k:
            res.append(heappop(arr)[1])
        return res  



if __name__ == '__main__':
    sol = Solution()
    sol.topKFrequentBucketSort()
    sol.topKFrequentMinHeap()
