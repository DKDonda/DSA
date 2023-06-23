class Solution:
    def missingNumber(self, nums) -> int:
        
        '''
        x = len(nums)
        shouldBeSum = (1+x)*x/2
        currentSum = sum(nums)
        ans = shouldBeSum-currentSum
        return int(ans)
        '''
        
        x = len(nums)
        return int(x*(x+1)/2 - sum(nums))