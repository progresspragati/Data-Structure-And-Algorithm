from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[len(nums)-1]):
            if i not in nums:
                return i
        return len(nums)

result = Solution()
print(result.missingNumber([0,1]))