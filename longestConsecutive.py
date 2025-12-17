from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums.sort()
        count = 1
        max = 1
        i = 1
        while i < len(nums):
            if(nums[i-1] + 1 == nums[i]):
                count += 1
                i += 1
            elif(nums[i-1] == nums[i] ):
                i += 1
            else:
                if(count > max):
                    max = count
                count = 1
                i += 1
        if(count > max):
            max = count
        return max
    
result = Solution()
print(result.longestConsecutive([2,20,4,10,3,4,5]))