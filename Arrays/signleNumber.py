'''
Given a non-empty array of integers nums, every element appears twice 
except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use 
only constant extra space.
'''
class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            newDict = {}
            for i in range (len(nums)):
                if(newDict[nums[i]] == None):
                    