class Solution:
    def minMoves(self, nums) -> int:
        ### this very long way without using maths.
        '''
        moves = 0
        lenNums = len(nums)
        while max(nums) != min(nums):
            moves += 1
            maxInd = nums.index(max(nums))
            for i in range(lenNums):
                if (i != maxInd):
                    nums[i] += 1
        print(moves) 
        return moves '''
        
        ### this is really shortest way
        return sum(nums) - len(nums)*min(nums)
    
a = Solution()
a.minMoves(nums=[1,2,3])