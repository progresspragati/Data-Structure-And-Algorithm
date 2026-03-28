from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0
        total_area = 0
        while left < right:
            total_area = min(heights[left], heights[right]) * (right-left)
            max_area = max(max_area, total_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

result = Solution()
print(result.maxArea([1,7,2,5,4,7,3,6]))
        
            
            
