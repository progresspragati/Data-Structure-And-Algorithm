from typing import List


class Solution:
    def robUsingRecursionPlusOneDP(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
        return dfs(0)
    
    def rob(self, nums:List[int])->int:
        if len(nums) ==0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        i =2
        while i < len(nums):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            i += 1
        return dp[i-1]
    def robSpaceOptimization(self, nums:List[int])->int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            newRob = max(rob2, nums[i]+rob1)
            rob1 = rob2
            rob2 = newRob
        return rob2
        
    
result = Solution()
# print(result.rob([2,9,8,3,6,1,2,9]))
print(result.robSpaceOptimization([2,9,8,3,6]))