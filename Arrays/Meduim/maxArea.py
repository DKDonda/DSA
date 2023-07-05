class Solution:
    def maxArea(self, height) -> int:
        ### This is brute force approach.
        """
        maxAmt = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                area = (j-i)*min(height[i],height[j])
                if area > maxAmt:
                    maxAmt = area
        return maxAmt
        """
        
        ### This one is using 2 pointers.
        p2 = len(height)-1
        p1 = 0
        maxAmt = 0
        while p1 < p2:
            area = (p2 - p1) * min(height[p1],height[p2])
            maxAmt = max(area, maxAmt)
            if height[p2] < height[p1]:
                 p2 -= 1
            else:
                p1 += 1
        return maxAmt