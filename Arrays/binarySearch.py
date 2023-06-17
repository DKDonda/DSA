'''
Search Insert Position
Given a sorted array of distinct integers and a target value, return the 
index if the target is found. If not, return the index where it would be 
if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

### This question gave me clear understanding of binary search in arrays.
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the target is found at the middle index
            if nums[mid] == target:
                return mid
            
            # If the target is greater, ignore the left half
            elif nums[mid] < target:
                left = mid + 1
            
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1

        # Target not found in the numsay
        if nums[mid] < target:
            return left
        else:
            return mid