class Solution:
    def longestPalindrome1(self, s: str) -> str:
        if len(s)==1:
            return s
        i = 1
        reslen = s[0]
        while i < len(s)-1:
            res = s[i]
            j = 1
            while i-j >= 0 and i+j <len(s) and s[i-j]==s[i+j]:
                res = s[i-j] + res + s[i+j]
                j += 1
            if len(reslen) < len(res):
                reslen = res
            i += 1
        i = 0
        while i < len(s)-1:
            if s[i] != s[i+1]:
                i += 1
                continue
            res = s[i]+s[i+1]
            j = 1
            while i-j >= 0 and i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                res = s[i-j]+res+s[i+j+1]
                j += 1
            if len(reslen) < len(res):
                reslen = res
            i += 1
        return reslen
    def longestPalindrome2(self, s: str) -> str:
        if len(s)==1:
            return s
        i = 1
        reslen = s[0]
        while i < len(s):
            res = s[i]
            res1 = ""
            j = 1
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                res = s[i-j] + res + s[i+j]
                j += 1
            k = 1
            while i-k >= 0 and i+k-1 < len(s) and s[i-j] == s[i+j-1]:
                res1 = s[i-k] + res1 + s[i+k-1]
                k += 1
            if len(res) >= len(res1):
                temp = res
            else:
                temp = res1
            if len(reslen) < len(temp):
                reslen = temp
            i += 1
        return reslen
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = 0
        max_len = 1
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        for i in range(len(s)):
            # for add palindrome
            l1, r1 = expand(i, i)
            # for even palindrome
            l2, r2 = expand(i, i+1)
            if r1-l1+1 > max_len:
                start = l1
                max_len = r1-l1+1
            if r2-l2+1 > max_len:
                start = l2
                max_len = r2-l2+1
        return s[start: start+max_len]


result = Solution()
print(result.longestPalindrome("abacd"))