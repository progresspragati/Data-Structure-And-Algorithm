from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root



result = Solution()
root = TreeNode(6)
nodeA = TreeNode(2)
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

print(result.lowestCommonAncestor(root, nodeA, nodeB))