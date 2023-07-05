""" Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. The 
relative order of the elements should be kept the same. Then return the 
number of unique elements in nums """

class Solution:
    def removeDuplicates(self, nums) -> int:
        ### This was using list and was of time complexity O(n2)
        """ count = 1
        i = 0
        while i < len(nums):
            if (nums[i+1] == nums[i]):
                nums.pop(i+1)
            else:
                count += 1
                i += 1 """
        ### This is using dictionary and time complexity is O(n)
        listToDict = {}
        for i in range(len(nums)):
            if listToDict.get(nums[i]) == None:
                listToDict[nums[i]] = 1
            else:
                listToDict[nums[i]] += 1
        keyList = list(listToDict.keys())   # these are nums
        valueList = list(listToDict.values())   # these are accurences
        for j in range(len(keyList)):
            iterations = valueList[j]
            if (iterations > 1):
                for k in range(iterations - 1):
                    nums.remove(keyList[j])
        print(nums)
        print(len(listToDict))
        return len(listToDict)
    
a = Solution()
a.removeDuplicates(nums = [1,1,2])