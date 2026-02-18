class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(1,(len(s))):
            if ord(s[i]) >= ord(s[i-1]):
                sum += ord(s[i]) - ord(s[i-1])
            else:
                sum += ord(s[i-1]) - ord(s[i])
        return sum
    
result = Solution()
print(result.scoreOfString("code"))