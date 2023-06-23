'''
    Given two binary strings a and b, return their sum as a binary string.
    
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"
'''
### Binary to integer knowledge check
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        this is standard method
        
        intA = int(a,2)
        intB = int(b,2)
        intC = intA + intB
        ans = str(bin(intC))
        return ans
        '''
    ### This is more efficient method
        """
        Pattern is this
        a=1 b=1 c=1 -> ans=1 c=1
        a=1 b=1 c=0 -> ans=0 c=1
        a=1 b=0 c=1 -> ans=0 c=1
        a=1 b=0 c=0 -> ans=1 c=0
        a=0 b=1 c=1 -> ans=0 c=1
        a=0 b=1 c=0 -> ans=1 c=0
        a=0 b=0 c=1 -> ans=1 c=0
        a=0 b=0 c=0 -> ans=0 c=0
        """
    ### So in such question use the consept of truth table. And code it.
        carry = 0
        iA = len(a) - 1
        iB = len(b) - 1
        ans = ''

        while (iA >= 0 or iB >= 0 or carry > 0):
            if iA >= 0:
                carry += int(a[iA])
                iA -= 1
            if iB >= 0:
                carry += int(b[iB])
                iB -= 1
            subAns = carry % 2
            carry = carry // 2
            ans = str(subAns) + ans
        return ans

a = Solution()
a.addBinary(a="11", b="1")