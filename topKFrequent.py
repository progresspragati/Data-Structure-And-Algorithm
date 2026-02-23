from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0)+1 
        sorted_items = sorted(result.items(), key=lambda x: x[1], reverse = True)
        return [item[0] for item in sorted_items[:k]]
        
result = Solution()
print(result.topKFrequent([1,2,2,3,3,3], k = 2))
