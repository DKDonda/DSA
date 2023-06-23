class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        keepGoing = True
        iA = len(a)
        iB = len(b)
        while keepGoing:
            if carry == 0:
                if (a[iA] == '0' and b[iB] == '0'):
                    ans = '0' + ans
                elif ((a[iA] == '1' and b[iB] == '0') or (a[iA] == '0' and b[iB] == '1')):
                    ans = '1' + ans
                elif (a[iA] == '1' and b[iB] == '1'):
                    ans = '0' + ans
                    carry = 1
            else:                ### if carry == 1:
                if (a[iA] == '0' and b[iB] == '0'):
                    ans = '1' + ans
                elif ((a[iA] == '1' and b[iB] == '0') or (a[iA] == '0' and b[iB] == '1')):
                    ans = '0' + ans
                    carry = 1
                elif (a[iA] == '1' and b[iB] == '1'):
                    ans = '1' + ans
                    carry = 1
            ### Now checking on keepGoing condition
            if (ca)
