class Solution:
    def rotate(self, matrix) -> None:
        left,right = 0,len(matrix)-1
        while left<right:
            for i in range(right-left):
                top, bottom = left, right
                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1
            
a = Solution()
print(a.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))