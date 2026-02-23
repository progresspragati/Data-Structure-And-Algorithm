from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = []
            if target-nums[i] in nums[i+1:len(nums)]:
                res.append(i)
                for j in range(i+1, len(nums)):
                    if nums[j] == target-nums[i]:
                        res.append(j)
                return res
        return []
    
    def twoSumUsingDict(self, nums:List[int], target: int)-> List[int]:
        res = {}
        for i in range(len(nums)):
            if target-nums[i] in res:
                return [res[target-nums[i]], i]
            res[nums[i]] = i
        return []

result = Solution()
print(result.twoSumUsingDict([3,4,5,6], 7))
        