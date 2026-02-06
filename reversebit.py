class Solution:
    def reverseBits(self, n: int) -> int:
        dp = [0]*32
        sum = 0
        base = 1
        for i in range(32):
            if (1 << i) & n:
                dp[i] = 1
        for i in range(31, -1, -1):
            sum +=  base * dp[i]
            base *= 2
        return sum
result = Solution()
print(result.reverseBits(0b00000000000000000000000000010101))
