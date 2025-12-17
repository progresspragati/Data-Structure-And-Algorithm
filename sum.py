from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i+1
        while(i < len(nums)-1):
            list_index = []
            if target - nums[i] == nums[j]:
                list_index.insert(0, i)
                list_index.insert(1, j)
                return list_index
            elif j == len(nums)-1:
                i += 1
                j = i+1
            else:
                j += 1
        return
    def twoSumOfElement(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums)-1:
            list_index = []
            if (target-nums[i]) in nums[i+1: ]:
                j = i+1
                while nums[j] != (target-nums[i]):
                    j += 1
                list_index.insert(0,i)
                list_index.insert(1,j)
                return list_index
            i += 1
        return


result = Solution()
print(result.twoSumOfElement([3,2,4], 6))
