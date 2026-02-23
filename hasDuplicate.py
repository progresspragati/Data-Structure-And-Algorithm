from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1: len(nums)]:
                return True
        return False

    def hasDuplicateUsingHashSet(self, nums: List[int])-> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)
        return False

result = Solution()
print(result.hasDuplicateUsingHashSet([1,2,3,4]))