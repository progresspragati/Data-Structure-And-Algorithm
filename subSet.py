from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dFS(i,nums,path):
            if i >= len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            dFS(i + 1, nums, path)
            path.pop()
            dFS(i + 1, nums, path)
        dFS(0, nums, path = [])
        return res
    
    def subset(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(i, path):
            res.append(path[:])
            for j in range(i, len(nums)):
                path.append(nums[j])
                backTrack(j+1, path)
                path.pop()
        backTrack(0, [])
        return res


result = Solution()
print(result.subsets([1,2,3]))
print(result.subset([1,2,3]))