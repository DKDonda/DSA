class Solution:
    def twoSum(self, numbers, target: int):
        pointer1 = 0
        pointer2 = len(numbers)-1
        while pointer1 < pointer2:
            if (numbers[pointer2] + numbers[pointer1] == target):
                return [pointer1+1, pointer2+1]
            elif (numbers[pointer2] + numbers[pointer1] > target):
                pointer2 -= 1
            else:
                pointer1 += 1
        return False