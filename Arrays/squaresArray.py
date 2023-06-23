'''
    I solved it using Two-Pointers. There are 5 different ways to
    solve it in leetcode. Please have a look at it.
    My solution T = O(N) and spave = O(1)
'''
class Solution:
    def sortedSquares(self, nums):
        pointerOne = 0
        x = len(nums)-1
        pointerTwo = x
        
        while pointerOne <= pointerTwo:
            sq1 = nums[pointerOne]**2
            sq2 = nums[pointerTwo]**2
            
            if sq2 >= sq1:
                nums.pop(pointerTwo)
                nums.insert(pointerTwo, sq2)
                pointerTwo -= 1
                
            else:
                nums.pop(pointerOne)
                nums.insert(pointerTwo, sq1)
                pointerTwo -= 1
        return nums
    
a = Solution()
print(a.sortedSquares(nums= [-4,-1,0,3,10]))