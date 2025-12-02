from typing import List


class Solution:
    def hasDuplicate_bruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False   
    def hasDuplicate_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False    
    def hasDuplicate_set(self, nums: List[int]) -> bool:
        a = set()
        for i in range(len(nums)):
            if nums[i] in a :
                return True
            else:
                a.add(nums[i])
        return False    
    def hasDuplicate_convertIntoSet(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) < len(nums):
            return True
        return False  
    

m = Solution()
print(m.hasDuplicate_convertIntoSet([1,2,3,3]))
