'''
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. The digits are 
    ordered from most significant to least significant in left-to-right 
    order. The large integer does not contain any leading 0's.
    
    This is a perfect recursion question using an array
'''
class Solution:
    def plusOne(self, digits):
        ### input = list
        lstInd = len(digits)-1
        if (digits[lstInd] != 9):
            digits[lstInd] += 1
            return digits
        else:
            digits[lstInd] = 0
            if (lstInd == 0):
                digits.insert(0,1)
                return digits
            else:
                return (self.plusOne(digits[:lstInd])+ [0])

a = Solution()
print(a.plusOne(digits = [9,9,9]))