from typing import List


class Solution:
    def eraseOverlapIntervalsUsingTopDownDP(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        memo = {}
        n = len(intervals)
        def dfs(i):  
            if i in memo:
                return memo[i]
            res = 1
            for j in range(i+1, n):
                if intervals[i][1] <= intervals[j][0]:
                    res = max(res, 1 + dfs(j))
                memo[i] = res
            print(memo)
            return res
        return (n - dfs(0))

    def eraseOverlapIntervalsUsingBottomUpDP(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        dp = [0]*n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1+dp[j])
        return n - max(dp)
    
    def eraseOverlapIntervalsUsingDPBinarySearch(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        dp = [0] * n
        intervals.sort(key = lambda x: x[1])
        dp[0] = 1
        def bs(r, target):
            l = 0
            while l < r:
                m = (l+r) >> 1
                if intervals[m][1] <= target:
                    l = m+1
                else:
                    r = m
            return l
        for i in range(1, n):
            idx = bs(i, intervals[i][0])
            if idx == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i], 1+dp[i-1])
        return n - dp[n-1]
    def eraseOverlapIntervalsUsingGreedySortByStart(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res
    
    def eraseOverlapIntervalsUsingGreedySortByEnd(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
    
result = Solution()
print(result.eraseOverlapIntervalsUsingGreedySortByEnd([[1,2],[2,4],[1,4]]))


        