### This Question gave me opportunity to use basic functions of array and look into time complexity

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)   ### O(n)
        ind = nums.index(maxNum)
        nums.remove(maxNum)  ### O(n)
        secondMax = max(nums)
        if maxNum >= 2*secondMax:
            return ind
        else:
            return -1