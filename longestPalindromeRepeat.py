class Solution:
    def longestPalindromeUsingBruteForce(self, s: str) -> str:
        res = ""
        reslen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l = i
                r = j
                while l < r and s[i] == s[j]:
                    l += 1
                    r -= 1
                if l >= r and reslen < j - i +1:
                    reslen = j - i + 1
                    res = s[i: j+1]
        return res
    
    def longestPalindromeUsingDp(self, s:str) -> str:
        resIndex = 0
        resLen = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < j-i+1:
                        resLen = j-i+1
                        resIndex = i
        return s[resIndex:resIndex+resLen]
    
    def longestPalindromeUsingTwoPointer(self, s:str) -> str:
        resIndex = 0
        resLen = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r-l+1:
                    resLen = r-l+1
                    resIndex = l
                l -= 1
                r += 1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r-l+1:
                    resLen = r-l+1
                    resIndex = l
                r += 1
                l -= 1
        return s[resIndex: resIndex+resLen]

    def longestPalindromeUsingManachar(self, s: str) -> str:
        def manachar(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l = 0
            r = 0
            for i in range(n):
                p[i] = min(r-i, p[l + r-i]) if l < r else 0
                while (i+p[i]+1 <n and i - p[i]-1 >= 0) and t[i + p[i] + 1] == t[i-p[i] -1]:
                    p[i] += 1
                if i+p[i] > r:
                    l , r = i - p[i], i + p[i]
            return p
        p = manachar(s)
        resLen, center_index = max((v,i) for i, v in enumerate(p))
        resIndex = (center_index-resLen)//2
        return s[resIndex: resIndex+resLen]

result = Solution()
print(result.longestPalindromeUsingManachar("ababd"))