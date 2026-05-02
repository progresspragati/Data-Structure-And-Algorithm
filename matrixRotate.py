from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][rows-i-1] = matrix[i][j]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = res[i][j]

    def rotateUsingFourCells(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) -1
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1

result = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
result.rotateUsingFourCells(matrix)
print(matrix)
