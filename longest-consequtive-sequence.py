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


        longest_sequence = 0

        #create a hashmap that stores each element of nums as key and false as their value
        hmap = {num: False for num in self.nums}
        
        for num in self.nums:

        #create forward check
            #for each num in iteration set current_sequence to 1
            #if there is no next or previous element sequence is 1
            current_sequence = 1

            #next element in the sequence will be num + 1
            next_element = num + 1
            
            #if next_element is in hmap and false, increment current_sequence and set hmap[next_element] True.
            #repeat until next_element not in the hmap or True
            while not hmap[next_element] and next_element in hmap:
                current_sequence += 1
                hmap[next_element] = True
                next_element += 1

        #create backward check
            #previous element in the sequence is num - 1
            prev_element = num - 1
            
            #if previous element in hmap and false, increment current_sequence and set hmap[next_element] True
            #repeat until previous element not in the hmap or False.
            while prev_element in hmap and not prev_element:
                current_sequence += 1
                hmap[prev_element] = True
                prev_element -= 1

        #set longest_sequence to the maximum of longest_sequence and current_sequence
        #this will set longest_sequence to current_sequence only if current_sequence is greater than longest_seq.
        
            longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

    def longestConsecutiveBruteForce(self) -> int:
        """
        Time Complexity & Space Complexity: O(N^2) 
        """
        pass


if __name__ == "__main__":
    pass


