from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for word in wordDict:
            t = max(t, len(word))
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for j in range(i, min(len(s), i+t)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
    
    def wordBreakBottomUp(self, s:str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        t = 0
        for w in wordDict:
            t = min(t, len(w))
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if t + i > len(s):
                    break
                if (i + len(w) <= len(s)) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

result = Solution()
print(result.wordBreakBottomUp("neetcode", ["neet", "code"]))

