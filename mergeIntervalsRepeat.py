from collections import defaultdict
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        res = []
        intervals.sort()
        res.append(intervals[0])
        while i < len(intervals):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res
    
    def mergeUsingSweepLineAlgorithm(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        res = []
        interval = []
        have = 0
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res

    def mergeUsingGreedy(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(mp[start], end + 1)
        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i]-1, have)
            if (have == i):
                res.append([interval_start, have])
                have = -1
                interval_start = -1
        if interval_start != -1:
            res.append([interval_start, have])
        return res


result = Solution()
print(result.mergeUsingGreedy([[1,3],[1,5],[6,7]]))