from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            dp[amount] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
    
    def coinChangeOptimal(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for amt in range(amount+1):
            for coin in coins:
                if amt-coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return dp[amount] if dp[amount] != amount+1 else -1
    

result = Solution()
print(result.coinChangeOptimal([1,2,5], 12))