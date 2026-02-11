from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visit_row = set()
        visit_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visit_row.add(i)
                    visit_col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in visit_row or j in visit_col:
                    matrix[i][j] = 0
        print(matrix)
result = Solution()
print(result.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))