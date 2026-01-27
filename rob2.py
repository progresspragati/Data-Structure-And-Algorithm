from typing import List


class Solution:
    def rob2(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        rob1= nums[1]
        rob2 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            newRob = max(rob2, nums[i]+rob1)
            rob1 = rob2
            rob2 = newRob
        res1 = rob2
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            newRob = max(rob2, rob1+nums[i])
            rob1 = rob2
            rob2 = newRob
        res2 = rob2
        if res1 >= res2:
            return res1
        return res2
        

result = Solution()
print(result.rob2([2,9,8,3,6]))