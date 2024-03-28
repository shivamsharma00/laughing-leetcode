'''
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Intuition
I have used sets which only store distinct values in them. Although lists can stores duplicate values.

Approach
I have created a set of nums list and compared the length of the list and set. If list would have duplicate values, its length will be greater than the set.

Complexity
Time complexity:
O(n) becaue code iterated through list once to create the set.
Space complexity:
O(n) where n is the size of input array nums.

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set)!=len(nums):
            return True
        return False