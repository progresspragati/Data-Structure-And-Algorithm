from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_int = []
        total = 1
        i = 0
        count_0 = 0
        for x in nums:
            if x != 0:
                total = total * x
            else:
                count_0 += 1
        while i < len(nums):
            if count_0 > 1:
                list_int.append(0)
            elif (count_0 == 1 and nums[i] != 0):
                list_int.append(0)
            elif nums[i] == 0:
                list_int.append(total)
            else:
                k = total / nums[i]
                list_int.append(int(k))
            i += 1
        return list_int
    
result = Solution()
print(result.productExceptSelf( [1,2,4,6]))