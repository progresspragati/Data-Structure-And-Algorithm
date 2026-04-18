class Solution:
    def longestCommonSubsequenceRecursion(self, text1: str, text2: str) -> int:
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            return max(dfs(i+1,j), dfs(i, j+1))
        return dfs(0,0)
    
    def longestCommonSubsequenceUsingDpTopDown(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[(i,j)]
        return dfs(0,0)
    
    def longestCommonSubSequenceUsingBottomUp(self, text1: str, text2: str) -> int:
        dp = [[]]
    
result = Solution()
print(result.longestCommonSubsequenceUsingDpTopDown("cat", "crabt"))