class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0,0)
    
    def uniquePathsBottomUp(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    def uniquePathsOptimalSpace(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
    
    def uniquePathsOptimal(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[j] += dp[j+1]
        return dp[0]
    
result = Solution()
print(result.uniquePathsOptimal(3,3))