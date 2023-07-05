class Solution:
    def productExceptSelf(self, nums):
        ans = [1]
        lenNums = len(nums)
        
        for i in range(1,lenNums):
            ans.append(nums[i-1] * ans[i-1])
        postfix = 1
        for j in range(lenNums-2,-1,-1):
                postfix *= nums[j+1] 
                ans[j] *= postfix
        return ans
    
a = Solution()
print(a.productExceptSelf(nums=[1,2,3,4] ))