### 'this is little bit using 2 pointers. I solved it using loop.
'''
import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorList = []
        for i in range(1,int(math.sqrt(n))+1):
            if (n%i == 0):
                factorList.append(i)
                if int(n/i) != i:
                    factorList.append(int(n/i))
        factorList.sort()
        if k > len(factorList):
            return -1
        else:
            return factorList[k-1]
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1,n+1):
            if n%i == 0:
                k -= 1
                if k==0:
                    return i
        return -1
                
a = Solution()
print(a.kthFactor(n=4, k=4))