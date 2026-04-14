from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            if (i >= len(nums)) or (i == len(nums)-1 and flag):
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            dp[i][flag] = max(dfs(i+1, flag) ,nums[i] + dfs(i+2, flag or i == 0))
            return dp[i][flag]
        return max(dfs(0, True), dfs(1, False))

    def robUsingBottomUp(self, nums:List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(num):
            if not num:
                return 0
            if len(num) == 1:
                return num[0]
            dp = [0] * len(num)
            dp[0] = num[0]
            dp[1] = max(num[0], num[1])
            for i in range(2, len(num)):
                dp[i] = max(dp[i-1], num[i] + dp[i-2])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))

    def robUsingBottomUpOptimal(self, nums:List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self,nums:List[int]):
        rob1 = 0
        rob2 = 0
        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

result = Solution()
print(result.robUsingBottomUpOptimal([2,9,8,3,6]))


