class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        count = 0
        lisMod = []
        for i in range(k):
            lisMod.append(0)
        for i in range(len(nums)):
            nums[i] %= k
            lisMod[nums[i]] += 1
        for i in range(k):
            
        return lisMod
a = Solution()
print(a.subarraysDivByK(nums=[4,5,0,-2,-3,1], k=5))