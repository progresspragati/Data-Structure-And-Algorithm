from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1)
        i = n
        while i > 0:
            res = 0
            j = i
            while j:
                j &= (j-1)
                res += 1
            bits[i] = res
            i -= 1
        return bits
    
result = Solution()
print(result.countBits(4))


