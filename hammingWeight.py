class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res
    def hammingWeight1(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res
    
    def hammingWeight2(self, n:int) -> int:
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res
    
result = Solution()
print(result.hammingWeight2(0b10111))