'''
    I first wrote the code with O(n^2) time complexity, and then
    changed it to O(n) complexity.
'''
class Solution:
    def pivotIndex(self, nums) -> int:
        pivot = 0
        length = len(nums)
        leftPart = 0
        rightPart = sum(nums)-nums[0]
        while pivot < length:
            if rightPart == leftPart:
                return pivot
            else:
                leftPart += nums[pivot]
                pivot += 1
                if pivot < length:
                    rightPart -= nums[pivot]
                else: 
                    rightPart = 0
        return -1

a = Solution()
a.pivotIndex(nums=[-1,-1,1,1,0])