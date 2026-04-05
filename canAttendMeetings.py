from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x: x.start)
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prevEnd:
                return False
            else:
                prevEnd = interval.end
        return True 
    
result = Solution()
intervals = [
    Interval(0,30),
    Interval(5,10),
    Interval(15,20)
]
print(result.canAttendMeetings(intervals))

