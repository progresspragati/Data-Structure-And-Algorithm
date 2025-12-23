from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                if intervals[i][1] <= intervals[i-1][1]:
                    intervals.remove(intervals[i])
                else:
                    intervals[i-1][1] = intervals[i][1]
                    intervals.remove(intervals[i])
            else:
                i += 1
        return intervals
    
result = Solution()
print(result.merge([[1,3],[1,5],[6,7]]))