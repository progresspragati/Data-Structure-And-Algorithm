from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = -float('inf')
        max_sum = -float('inf')
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
result = Solution()
print(result.maxSubArray([2,-3,4,-2,2,1,-1,4]))