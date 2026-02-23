from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        max_string = 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                max_string += 1
            else:
                res = max(max_string, res)
                max_string = 1
        return max(max_string, res)
    
    def longestConsecutiveUsingHashMap(self, nums: List[int]) -> int:
        longest = 0
        res = set(nums)
        for num in nums:
            if num-1 not in res:
                current = num
                streak = 1
                while current+1 in res:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest

result = Solution()
print(result.longestConsecutiveUsingHashMap([2,20,4,10,3,4,5]))       




    