from typing import List

class Solution:
    def min(self, a, b)->int:
        return b if a > b else a 

    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        left = 1
        right = len(heights)-1
        max = abs(self.min(heights[0], heights[right])*(0 - right))
        while left < len(heights)-1:
            if heights[left] < heights[left-1]:
                left += 1
                continue
            right = len(heights)-1
            while right > left:
                area = abs(self.min(heights[left], heights[right])*(left - right))
                if(area > max):
                    max = area
                right -= 1
                if heights[right] < heights[right+1]:
                    right -= 1
            left += 1

        return max
    def maxArea2(self, heights: list[int])-> int:
        left = 0
        right = len(heights)-1
        max = 0
        while left < right:
            area = self.min(heights[left], heights[right]) * (right - left)
            if(area > max):
                max = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 
        return max

result = Solution()
nums = [5,1,5]
print(result.maxArea2(nums))