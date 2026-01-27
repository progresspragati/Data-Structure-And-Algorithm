from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        goal = len(nums)-1
        num = 0
        while i <= num:
            print(i)
            num = max(num, i + nums[i])
            if num >= goal:
                return True
            i += 1

        return False
    
result = Solution()
print(result.canJump([1,2,1,0,1]))