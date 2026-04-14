from typing import List


class Solution:
    def existUsingBackTrackingHashSet(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (min(r,c) < 0 or r >= rows or c >= cols or (r,c) in path or word[i] != board[r][c]):
                return False
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                  dfs(r-1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

    def existUsingBackTrackingUsingVisitedArray(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= rows or c >= cols or visited[r][c] or word[i] != board[r][c]):
                return False
            visited[r][c] = True
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            visited[r][c] = False
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
    
    def existUsingBackTrackingOptimal(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (min(r,c) < 0 or r >= rows or c >= cols or board[r][c] == "#" or word[i] != board[r][c]):
                return False
            board[r][c] = "#"
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            board[r][c] = word[i]
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

result = Solution()
matrix = [["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]]
print(result.existUsingBackTrackingOptimal(matrix, "CAT"))