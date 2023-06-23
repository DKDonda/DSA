### Best question to clearify the concept of Floating Numbers. 
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False

        x = math.log(n,2)
        y = int(math.log(n,2))
        
        if x > 1:
            if 2**y == n: return True
            else: False
        return not abs(x-y) > 0 
    
a = Solution()
print(a.isPowerOfTwo(n=536870912))