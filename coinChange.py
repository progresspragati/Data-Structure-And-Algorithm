from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i and dp[i-coin] != amount+1:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] == amount+1:
            return -1
        return dp[amount]

result = Solution()
print(result.coinChange([11, 22, 33, 44, 55, 66, 77, 88, 99, 111], 330))
        
        
