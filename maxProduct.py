from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        leftProduct = nums[0]
        rightProduct = nums[len(nums)-1]
        largest_product = max(leftProduct, rightProduct)
        for i in range(1,len(nums)):
            if leftProduct == 0:
                leftProduct = 1
            if rightProduct == 0:
                rightProduct = 1
            leftProduct *= nums[i]
            rightProduct *= nums[len(nums)-1-i]
            largest_product = max(largest_product, max(leftProduct, rightProduct))
        return largest_product

result = Solution()
print(result.maxProduct([1,2,-3,4]))
