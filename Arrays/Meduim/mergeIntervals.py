### A very good question to learn use of sort() and lambda efficiently.
class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]
        size = len(intervals)
        for i in range (1,size):
            if intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max (merged[-1][1], intervals[i][1])
        return merged
a = Solution()
print(a.merge(intervals= [[1,3],[2,6],[8,10],[15,18]]))