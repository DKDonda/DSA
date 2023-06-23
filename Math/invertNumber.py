class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        strNum = str(x)
        if (x >= 0):
            for i in range(len(strNum)):
                ans = strNum[i] + ans
        else:
            for i in range(1,len(strNum)):
                ans = strNum[i] + ans
            ans = '-'+ans
        if(int(ans) >= -2**31 and int(ans) <= 2**31 - 1):
            return int(ans)
        else:
            return 0