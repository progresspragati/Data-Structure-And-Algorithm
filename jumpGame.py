from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not 0 in nums:
            return True
        final_position = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= final_position:
                final_position = i
        return final_position == 0

result = Solution()
print(result.canJump([1,2,1,0,1]))