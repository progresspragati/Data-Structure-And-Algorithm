from typing import List
from collections import deque

class Solution:
    def numIslandsUsingDfs(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" :
                return
            grid[i][j] = "0" 
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        if len(grid) == 0:
            return 0
        islands_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands_count += 1
        
        return islands_count
    
    def numIslandsUsingBfs(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        islands_count = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # mark visited
            while queue:
                x, y = queue.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < rows and
                        0 <= ny < cols and
                        grid[nx][ny] == "1"
                    ):
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands_count += 1
        return islands_count
     
    
result = Solution()
print(result.numIslandsUsingBfs([["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]))