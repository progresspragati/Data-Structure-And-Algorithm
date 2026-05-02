from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                i = i & (i-1)
                count += 1
            res.append(count)
        return res
    
    def countBitsUsingBuiltInFunction(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]

result = Solution()
print(result.countBitsUsingBuiltInFunction(4))