from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        for num in nums:
            sum = sum + num
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0
        return maxSum    

result = Solution()
print(result.maxSubArray([-2,-1]))