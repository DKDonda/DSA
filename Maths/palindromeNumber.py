class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        else:
            strX = str(x)
            for i in range(len(strX)//2):
                if (strX[i] != strX[len(strX)-1-i]):
                    return False
            return True