### Given a string s, find the length of the longest substring without 
# repeating characters.

### abcadfbbcsdfgh

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count1 = 2
        count2 = 2
        startIndex = 0
        endIndex = 1
        while endIndex < len(s) and startIndex<=endIndex:
            if (endIndex<len(s)-1):
                if s[endIndex] == s[endIndex+1]:
                    startIndex = endIndex + 1
                    endIndex = startIndex + 1
                    if (count1 > count2):
                        count2 = count1
                    count1 = 2
                elif s[startIndex] != s[endIndex]:
                    count1 += 1
                    endIndex += 1
                else:
                    startIndex += 1
                    count1 -= 1

        print(count2)
        return count2

a = Solution()
a.lengthOfLongestSubstring(s = "pwwkew")