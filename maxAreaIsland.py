from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if (min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        return area
    
    def maxAreaOfIslandUsingBfs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        area = 0
        def bfs(r,c):
            queue = deque()
            grid[r][c] = 0
            queue.append((r,c))
            res = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if (min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    queue.append((nr,nc))
                    res += 1
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area

result = Solution()
grid = [[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
print(result.maxAreaOfIslandUsingBfs(grid))


