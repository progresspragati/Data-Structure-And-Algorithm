from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def getMax(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        path = root.val + max(left, right)
        return max(0, path)
    
    def maxPathSumOptimal(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res
    
result = Solution()
node1 = TreeNode(-15)
node2 = TreeNode(10)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(-5, None, None)
node6 = TreeNode(5, None, None)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node6
node4.left = node5
print(result.maxPathSumOptimal(node1))
