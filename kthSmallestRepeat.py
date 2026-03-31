from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node:Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]
    
    def kthSmallestOptimal(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val
        def dfs(node:Optional[TreeNode]):
            nonlocal count, res
            if not node:
                return
            dfs(node.left)
            count -= 1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
    
    def kthSmallestOptimalIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

result = Solution()
nodeA = TreeNode(2)
nodeB = TreeNode(1)
nodeC = TreeNode(3)
nodeA.left = nodeB
nodeA.right = nodeC
print(result.kthSmallestOptimalIterative(nodeA, 1))