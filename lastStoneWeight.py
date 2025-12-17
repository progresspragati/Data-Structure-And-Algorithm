import heapq
from typing import List

class Solution:
    def lastStoneWeightUsingSort(self, stones: List[int]) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x < y:
                y = y-x
                stones.append(y)
        if len(stones) == 0:
            return 0 
        return stones[0]
    
    def lastStoneWeight(self, stones: list[int])-> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, y-x)
        if len(stones) == 0:
            return 0
        return abs(stones[0])


result = Solution()
stones = [1,2]
print(result.lastStoneWeight(stones))
            
        