from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left+1
        max_profit = 0
        while right < len(prices):
            max_profit = max( prices[right] - prices[left], max_profit)
            if prices[left] >  prices[right]:
                left = right
            right += 1
        return max_profit
    
result = Solution()
print(result.maxProfit([2,1,2,1,0,1,2]))
            


        