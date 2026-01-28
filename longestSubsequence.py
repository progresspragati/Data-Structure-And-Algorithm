from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        dp[0] = 1
        
        i = 0
        j = i+1
        max_length = 1
        while j < len(nums):
            if i == j:
                i = 0
                j += 1
                continue
            elif nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i]+1)
            i += 1
        for i in range(len(dp)):
            max_length = max(max_length, dp[i])
        return max_length
    
result = Solution()
print(result.lengthOfLIS([0,3,1,3,2,3]))
