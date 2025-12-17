
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()
        for ch in s:
            while ch in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(ch)
            max_length = max(max_length, len(char_set))
        return max_length
    
result = Solution()
print(result.lengthOfLongestSubstring2("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"))
