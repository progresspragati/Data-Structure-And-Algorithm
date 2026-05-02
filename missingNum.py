from typing import List


class Solution:
    def missingNumberUsingSort(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumberUsingHashSet(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

    def missingNumberUsingXorr(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr

    def missingNumberUsingMath(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res
    
result = Solution()
print(result.missingNumberUsingMath([1,2]))