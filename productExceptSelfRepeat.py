from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        i = 0
        res = []
        for num in nums:
            if num == 0 and i == 0:
                i += 1
                continue
            if num == 0 and i == 1:
                product = 0
                break
            product *= num
        print(product)
        print(i)
        for num in nums:
            if num == 0:
                res.append(product)
            elif i > 0:
                res.append(0)
            else:
                res.append(product//num)
        return res
    
    def productExceptSelfUsingPrefixSufix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = suffix[n-1] = 1
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

    def productExceptSelfOptimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        suffix = 1
        for i in range(n-1, -1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


result = Solution()
print(result.productExceptSelfOptimal([1,2,3,4]))
            