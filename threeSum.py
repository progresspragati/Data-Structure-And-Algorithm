from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res_triplet = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left]+nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left]+nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    res_triplet.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left+= 1
                    right -= 1
        return res_triplet
    
result = Solution()
print(result.threeSum([0,0,0,0]))


        