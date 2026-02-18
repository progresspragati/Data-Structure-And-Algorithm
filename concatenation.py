from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
    
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        ans = nums
        ans.extend(nums)
        return ans
    
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums + nums

result = Solution()
print(result.getConcatenation1([1,2,3,4]))
