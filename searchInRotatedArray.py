from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        count = 0
        if target not in nums:
            return -1
        while nums[left] != target:
            nums = nums[1:] + nums[:1]
            count += 1
        return count

result = Solution()
print(result.search([3,5,6,0,1,2], 4))