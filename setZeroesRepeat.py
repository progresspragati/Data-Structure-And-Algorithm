from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        copy = [[matrix[r][c] for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for row in range(rows):
                        copy[row][c] = 0
                    for col in range(cols):
                        copy[r][col] = 0
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = copy[r][c]
    
    def setZeroesUsingIteration(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [False] * m
        cols = [False] * n
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for r in range(m):
            for c in range(n):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
    
result = Solution()
matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
result.setZeroesUsingIteration(matrix)
print(matrix)
                    