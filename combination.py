from ast import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(i, path, sum):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                backTrack(j, path, sum+nums[j])
                path.pop()
        backTrack(0, [], 0)
        return res

result = Solution()
print(result.combinationSum([2,5,6,9], 9))