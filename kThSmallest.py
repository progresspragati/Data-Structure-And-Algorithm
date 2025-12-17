from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack  = [root]
        nums = []
        while stack:
            node = stack.pop()
            nums.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        nums.sort()
        return nums[k-1]

result = Solution()
root = TreeNode(6)
nodeA = TreeNode(7)
nodeB = TreeNode(8)
nodeC = TreeNode(0)
nodeD = TreeNode(4)
nodeE = TreeNode(7)
nodeF = TreeNode(9)

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
print(result.kthSmallest(root, 3))