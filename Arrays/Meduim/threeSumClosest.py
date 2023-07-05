class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        closest = 0
        closeseDiff = abs(closest-target)
        lenNums = len(nums)
        for i in range(lenNums-2):
            pointer1 = i+1
            pointer2 = lenNums-1
            
            while pointer1 < pointer2:
                summation = nums[i]+nums[pointer1]+nums[pointer2]
                currentDiff = abs(summation-target)
            
                if summation > target:
                    pointer2 -= 1
                elif summation < target:
                    pointer1 += 1
                else:
                    return target
                if currentDiff == min(currentDiff, closeseDiff):
                    closest = summation
                    closeseDiff = currentDiff
                
        return closest

a = Solution()
a.threeSumClosest(nums=[-1,2,1,-4], target=1)