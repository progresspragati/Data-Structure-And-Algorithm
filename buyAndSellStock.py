
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if(min_price > price):
                min_price = price
            else:
                max_profit = max(max_profit, (price - min_price))
        return max_profit
            


result = Solution()
prices = [2,1,2,1,0,0,1]
print(result.maxProfit(prices))