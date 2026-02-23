class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = 0
        for j in range(len(s)):
            if i >= len(t):
                return False
            for k in range(i, len(t)):
                if s[j] == t[k]:
                    i = k+1
                    break
                elif len(s)-j > len(t)-k:
                    return False
                elif k == len(t)-1 and s[j] != t[k]:
                    return False
        return True

result = Solution()
print(result.isSubsequence("aec", "abcde"))

