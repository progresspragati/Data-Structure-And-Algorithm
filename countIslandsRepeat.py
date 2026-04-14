from collections import deque
from typing import List


class Solution:
    def numIslandsUsingMatrixDfs(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def dfs(r,c):
            if (min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands

    def numIslandsUsingMatrixBfs(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
    
result = Solution()
grid = [["0","1","1","1","0"],["0","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(result.numIslandsUsingMatrixBfs(grid))