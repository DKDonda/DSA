class Solution:

### That was a brute force approach with O(n^2)
    '''def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return([i,j])
a = Solution()
a.twoSum(nums = [2,7,11,15], target = 9)'''

### Lets try that using hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i   

        for j in range(len(nums)):
            secondPart = target - nums[j]
            if secondPart in hashmap and hashmap[secondPart] != j:
                return (j,hashmap[secondPart])
a = Solution()
a.twoSum(nums = [2,7,11,15], target = 9)