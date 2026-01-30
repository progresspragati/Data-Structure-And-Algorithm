from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        i = 0
        j = i+1
        while j < len(nums):
            if i == j:
                i = 0
                j += 1
                continue
            elif nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i]+1)
            i += 1
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
result = Solution()
print(result.lengthOfLIS([0,3,1,3,2,3]))
