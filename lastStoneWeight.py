from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
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
    
result = Solution()
stones = [1,2]
print(result.lastStoneWeight(stones))
            
        