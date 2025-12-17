from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while nums[left] > nums[right]:
            nums = nums[-1:] + nums[:-1]
        return nums[0]
            
result = Solution()
print(result.findMin([4,5,6,7]))