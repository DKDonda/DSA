class Solution:
    def spiralOrder(self, matrix):
        left = 0
        top = 0
        bottom = len(matrix)
        right = len(matrix[0])
        ans = []
        
        while left < right and top < bottom:
            for i in range(left,right):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right -= 1
            
            if not (left<right and top<bottom):
                break
            
            for i in range(right-1, left-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
        return ans
a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])),