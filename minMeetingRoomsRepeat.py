from collections import defaultdict
import heapq
from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            print(min_heap)
        return len(min_heap)
    
    def minMeetingRoomsUsingSweepLine(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res

    def minMeetingRoomsUsingTwoPointer(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res = 0
        count = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

    def minMeetingRoomsUsingGreedy(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        time.sort(key = lambda x: (x[0], x[1]))
        res = 0
        count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
                  
result = Solution()
intervals = [
    Interval(0,30),
    Interval(5,10),
    Interval(15,20)
]
print(result.minMeetingRoomsUsingGreedy(intervals))