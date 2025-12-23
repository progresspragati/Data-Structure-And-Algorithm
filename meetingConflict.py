from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda i:i.start)
        i = 1
        while i < len(intervals):
            a = intervals[i-1]
            b = intervals[i]
            if a.end < b.start:
                return False
            i += 1
        return True

result = Solution()
intervals = [
    Interval(0, 30),
    Interval(5, 10),
    Interval(15, 20)
]
print(result.canAttendMeetings(intervals))
            
