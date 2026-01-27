class Solution:
    def countSubstrings(self, s: str) -> int:
        i = 0
        num_palindromes = 0
        while i < len(s):
            j = 1
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                num_palindromes += 1
                j += 1
            j = 1
            while i-j >= 0 and i+j-1 < len(s) and s[i-j] == s[i+j-1]:
                num_palindromes += 1
                j += 1
            i += 1
            num_palindromes += 1
        return num_palindromes
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = 0
        max_len = 1
        num_string = 0
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
print(result.countSubstrings("aaa"))