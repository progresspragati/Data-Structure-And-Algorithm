from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        max_word = 0
        for word in wordDict:
            max_word = max(len(word), max_word)
        
        for i in range(1,len(s)+1):
           for j in range(max(0, i - max_word), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                j -= 1
        return dp[len(s)]
    
result = Solution()
print(result.wordBreak("catsincars", ["cats","cat","sin","in","car"]))
