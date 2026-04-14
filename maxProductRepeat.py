from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = []
        cur = []
        res = float('-inf')
        for num in nums:
            res = max(res, num)
            if num == 0:
                if cur:
                    a.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur:
            a.append(cur)
        for sub in a:
            negs = sum(1 for i in sub if i < 0)
            need = negs if negs % 2 == 0 else negs -1
            prod = 1
            negs = 0
            j = 0
            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)
        return res

    def maxProductUsingKadaneAlgorithm(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        for num in nums:
            temp = curMax * num
            curMax = max(num, temp, curMin * num)
            curMin = min(num, curMin* num, temp)
            res = max(res, curMax)
        return res

    def maxProductUsingPrefixSuffix(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        prefix = 0
        suffix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-1-i] * (suffix or 1)
            res = max(res,max(prefix, suffix))
        return res

result = Solution()
print(result.maxProductUsingPrefixSuffix([1,2,-3,4]))
        
