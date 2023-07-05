class Solution:
    ### It's done by Memoization in Time Comp O(n) and Space Comp O(1)
    def runningSum(self, nums):
        runningSum = [nums[0]]
        for i in range(1,len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])
        return runningSum
    ### It can also be done in Time Comp O(n) and Space Comp O(1)
    ### by using In-Plce updation.
    """
    def runningSum(self, nums: List[int]) -> List[int]:
	for i in range(1,len(nums)):
		nums[i] = nums[i-1] + nums[i]
	return nums
    """