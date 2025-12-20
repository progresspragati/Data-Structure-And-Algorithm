from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def backTrack(r, c, i):
            if i == len(word):
                return True
            if (min(r,c) < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (backTrack(r+1, c, i+1) or
                   backTrack(r-1, c, i+1) or
                   backTrack(r, c+1, i+1) or
                   backTrack(r, c-1, i+1))
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if backTrack(r,c,0):
                    return True
        return False

result = Solution()
print(result.exist([
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
], "CAT"))
            
            