'''
    Pascal's Triangle
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
### This is an easy implementation of 2D Array

class Solution:
    def generate(self, numRows: int):
        if (numRows>=0):
            ans = []
        
        for i in range(1,numRows+1):
            if (i==1):
                ans = [[1]]
            if (i==2):
                ans = [[1],[1,1]]
            if (i>=3):
                sub = [1]
                for j in range(i-2):
                    adding = ans[i-2][j] + ans[i-2][j+2]
                    sub.append(adding)
                sub.append(1)
                ans.append(sub)
        return ans