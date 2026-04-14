class Solution:
    def countSubstringsBruteForce(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l = i
                r = j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                res += (l>=r)
        return res

    def countSubstringsUsingDp(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ( j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res

    def countSubstringsUsingTwoPointer(self, s:str) -> int:
        res = 0
        n = len(s)
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l = i
            r = i +1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
    
    def countSubstringsUsingTwoPointerOptimal(self, s:str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            res += self.countPali(s,i, i)
            res += self.countPali(s,i, i+1)
        return res
    def countPali(self, s:str, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            res += 1
        return res
    
result = Solution()
print(result.countSubstringsUsingTwoPointerOptimal("aaa"))