from typing import List


class Solution:
    def robUsingTopDownDfs(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
        return dfs(0)
    
    def robUsingBottomUpDfs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in  range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]
    
    def robOptimal(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = rob1
            rob1 = rob2
            rob2 = max(rob1, nums[i] + temp)
        return rob2

result = Solution()
print(result.robOptimal([2,9,8,3,6]))