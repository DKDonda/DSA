class Solution:
    def majorityElement(self, nums) -> int:
        """ countDict = {}
        n = len(nums)
        if n ==1 : return nums[0]
        for i in range(n):
            if countDict.get(nums[i]) != None:
                countDict[nums[i]] += 1
                if countDict[nums[i]] > n//2:
                    return nums[i]
            else:
                countDict[nums[i]] = 1 """
        candidate = -1
        votes = 0
        n = len(nums)
        ### Part 1 of the the Moore's Voting algorithm... 
        ### To find Candidate solution.
        for i in range(n):
            if votes != 0:
                if candidate == nums[i]:
                    votes += 1
                else:
                    votes -= 1
            else:
                votes = 1
                candidate = nums[i] 
                
        ### Part 2 of Moore's Voting Algorithm
        ### To verify if candidate solution is the final required sol
        count = 0
        for j in range(n):
            if candidate == nums[j]:
                count += 1
            if count > n//2:
                return candidate
        return -1
    
a = Solution()
print(a.majorityElement(nums=[2,2,1,1,1,2,2]))