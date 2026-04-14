import math


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    def climbStairsUsingDfs(self, n:int) -> int:
        dp = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if dp[i] != -1:
                return dp[i]
            dp[i] =  dfs(i+1) + dfs(i+2) 
            return dp[i]
        return dfs(0)
    
    def climbstairsUsingSpaceOptimization(self, n:int) -> int:
        prev = 1
        curr = 1
        for i in range(n-1):
            temp = prev
            prev = curr
            curr = temp+prev
        return curr

    def climbstairsOptimal(self, n:int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1+sqrt5)/2
        psi = (1-sqrt5)/2
        n += 1
        return round((phi**n + - psi**n)/sqrt5)
        
result = Solution()
print(result.climbstairsUsingSpaceOptimization(4))
print(result.climbstairsOptimal(4))