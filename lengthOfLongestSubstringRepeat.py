class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        max_length = 1
        max_string = s[0:1]
        while right < len(s):
            if s[right] in max_string:
                left += 1
                max_string = s[left: right]
            else:
                right += 1
                max_string = s[left: right]
                max_length = max(max_length, len(max_string))
        return max_length
    
result = Solution()
print(result.lengthOfLongestSubstring(" "))
            