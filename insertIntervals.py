from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
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
print(result.insert([[1,3],[4,6]], [2,5]))