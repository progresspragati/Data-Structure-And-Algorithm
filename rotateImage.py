from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-j-1]
                matrix[n-1-i][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = temp
        print(matrix)
result = Solution()
print(result.rotate([[1,2],[3,4]]))