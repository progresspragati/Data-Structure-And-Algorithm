from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            LIS = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            dp[i] = LIS
            return LIS
        return max(dfs(i) for i in range(n))

    def lengthOfLISBottomUp(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
    
    def lengthOfLISDPBinarySearch(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue
            index = bisect_left(dp, nums[i])
            dp[index] = nums[i]
        return LIS
             
result = Solution()
print(result.lengthOfLISDPBinarySearch([9,1,4,2,3,3,7]))