class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)
        return res

    def reverseBits2(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res * 2 + (n & 1)
            n = n >> 1
        return res
    
result = Solution()
print(result.reverseBits2(0b00010101))