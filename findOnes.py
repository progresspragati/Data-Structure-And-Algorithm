class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
    def hammingWeightLeftOperator(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count
    
    def hammingWeightUsingLeftOperator(self, n: int)-> int:
        count = 0
        while n:
            count += 1 & n
            n = n >> 1
        return count

result = Solution()
print(result.hammingWeightUsingLeftOperator(0b000000100100100100))