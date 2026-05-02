class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xffffffff
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)
        if res > 0x7fffffff:
            res = ~(res ^ mask)
        return res

    def getSum2(self, a:int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a < max_int else ~(a ^ mask)

result = Solution()
print(result.getSum2(1,1))

