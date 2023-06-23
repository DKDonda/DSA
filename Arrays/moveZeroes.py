class Solution:
    def moveZeroes(self, nums) -> None:
        ### This fails for nums = [0,0,1]
        '''
        x = len(nums)
        for i in range(x):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(x-1,0) '''
        ### hence we need 2 pointers
        ### Try with this examples [0,0,1,4,0,8,0]
        slow = 0
        for fast in range(len(nums)):
            if nums[slow]==0 and nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                
            if nums[slow] != 0:
                slow += 1 