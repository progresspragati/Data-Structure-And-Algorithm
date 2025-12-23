from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        num_overlap = 0
        i = 1
        prev_end = intervals[0][1]
        while i < len(intervals):
            if prev_end > intervals[i][0]:
                num_overlap += 1
                prev_end = min(intervals[i][1], prev_end)
            else:
                prev_end = intervals[i][1]
            i += 1
        print(intervals)
        return num_overlap
    
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # overlap → remove current interval
                count += 1
            else:
                # no overlap → keep interval
                prev_end = intervals[i][1]

        return count

result = Solution()
print(result.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
        