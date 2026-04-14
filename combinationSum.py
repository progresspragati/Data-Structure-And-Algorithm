from typing import List


class Solution:
    def combinationSumUsingBackTracking(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr_list.append(nums[i])
            dfs(i, curr_list, total+nums[i])
            curr_list.pop()
            dfs(i+1, curr_list, total)
        dfs(0, [], 0)
        return res

    def combinationSumUsingBackTrackingOptimal(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            for j in range(i, len(nums)):
                if total > target:
                    return
                curr_list.append(nums[j])
                dfs(j, curr_list, total+nums[j])
                curr_list.pop()
        dfs(0, [], 0)
        return res
    
result = Solution()
print(result.combinationSumUsingBackTrackingOptimal([2,5,6,9], 9))

        