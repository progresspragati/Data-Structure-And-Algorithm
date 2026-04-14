from collections import deque
from typing import List


class Solution:
    def pacificAtlanticUsingDfs(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        atl = set()
        pac = set()
        def dfs(r,c,visit,prevHeights):
            if (min(r,c) < 0 or c >= cols or r >= rows or (r,c) in visit or heights[r][c] < prevHeights):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        res = []
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        print(atl)
        print(pac)
        return res

    def pacificAtlanticUsingBfs(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        def bfs(source, ocean):
            queue = deque((source))
            while queue:
                x, y = queue.popleft()
                ocean[x][y] = True
                for dr, dc in directions:
                    nr = x+dr
                    nc = y + dc
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and not ocean[nr][nc] and heights[x][y] <= heights[nr][nc]):
                        queue.append((nr,nc))
        res = []       
        pacific = []
        atlantic = []
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols-1))
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1, c))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res

result = Solution()
heights = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
print(result.pacificAtlanticUsingBfs(heights))

        