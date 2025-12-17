from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_list = []
        nums.sort()
        left = 0
        next = left + 1
        next_next = next + 1
        while next + 1 < len(nums):
            temp_list = []
            sum = nums[left] + nums[next] + nums[next_next]
            if sum == 0:
                temp_list.append(nums[left])
                temp_list.append(nums[next])
                temp_list.append(nums[next_next])
                if temp_list not in triplet_list:
                    triplet_list.append(temp_list)
                if (next_next+1 == len(nums)):
                    left += 1
                    next += 1
                    next_next = next + 1
                else: 
                    left += 1
                    next += 1
                    next_next += 1
            elif sum < 0:
                if (nums[left] + nums[next]) <= nums[next_next]:
                    next_next += 1
                    if (next_next == len(nums)):
                       left += 1
                       next += 1
                       next_next = next + 1 
            else:
                return triplet_list
        return triplet_list
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        triplet_list = []
        nums.sort()
        i = 0
        while i < len(nums)-2:
            left = i+1
            right = len(nums)-1
            while left < right:
                temp_list = []
                if (nums[left] + nums[right]) +nums[i] == 0:
                    temp_list.append(nums[i])
                    temp_list.append(nums[left])
                    temp_list.append(nums[right])
                    if temp_list not in triplet_list:
                        triplet_list.append(temp_list)
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right])+ nums[i] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
        return triplet_list



result = Solution()
nums = [-2,0,1,1,2]
# result.threeSum2(nums)
print(result.threeSum2(nums))
