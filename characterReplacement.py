class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_char_set = set(s)
        res = 0
        for char in unique_char_set:
            count = 0
            left = 0
            for right in range(len(s)):
                if s[right] == char:
                    count += 1
                while (right-left+1)-count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                res = max(res, right-left+1)
        return res  
        
result = Solution()
print(result.characterReplacement("BAAAB", 2))
