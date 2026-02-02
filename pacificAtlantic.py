from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if((r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r, c) in atlantic:
                    res.append([r,c])
        return res
    
    def pacificAtlanticUsingBfs(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        pac = [[False] * cols for _ in range(rows)] 
        atl = [[False] * cols for _ in range(rows)] 

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr >=0 and nr < rows and nc >= 0 and nc < cols and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        q.append((nr,nc))

        pacific = []
        atlantic = []
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        
        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        res = []

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res


    
result = Solution()
print(result.pacificAtlanticUsingBfs([
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]))