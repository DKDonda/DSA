class Solution:
    def threeSum(self, nums):
        nums.sort()
        lenNum = len(nums)
        l=[]
        for i in range(lenNum-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i+1
            k = lenNum-1
            while j < k:
                summation = nums[i] + nums[j] + nums[k]
                if summation < 0:
                    j += 1
                elif summation > 0:
                    k -= 1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j<k:
                        j += 1
        return l