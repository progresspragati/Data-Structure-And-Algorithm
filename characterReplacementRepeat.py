class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count_freq = {}
        res = 0
        max_freq = 0
        for right in range(len(s)):
            count_freq[s[right]] = 1 + count_freq.get(s[right], 0)
            max_freq = max(max_freq, count_freq[s[right]])
            while (right - left + 1) - max_freq > k:
                count_freq[s[left]] -= 1
                left += 1
            res = max(res, right - left +1)
        return res

result = Solution()
print(result.characterReplacement("XYXY", 2))