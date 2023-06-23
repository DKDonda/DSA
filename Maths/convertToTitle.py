''' 
    A very Good Question. Mathematical
'''
import math

class Solution:
    def find_x(self, colNum):
        x = 1
        while True:
            lower_bound = (26**x - 1)/(25)
            upper_bound = 26*(26**(x) -1)/25
            if lower_bound <= colNum <= upper_bound:
                return x
            x += 1
    
    def findAlphaInt(self, colNum, x):
        k = 1
        while True:
            lower_bound = ((26**(x) - 1)/25) + (k-1)*(26**(x-1))
            upper_bound = ((26**(x) - 1)/25) + k*(26**(x-1)) - 1
            if lower_bound <= colNum <= upper_bound:
                return k
            k += 1
        
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        ### Number of Characters
        numberOfChars = self.find_x(columnNumber) 
        n = columnNumber 
        for i in range(numberOfChars,0,-1):
            firstAlphaInt = self.findAlphaInt(n, i)
            ans += chr(64 + firstAlphaInt)
            n -= 26**(i)    ### only have to fix here now.
        print(ans)
        return ans
a = Solution()
a.convertToTitle(columnNumber=28)