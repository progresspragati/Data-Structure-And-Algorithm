from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append((root, float('-inf'), float('inf')))

        while queue:
            node, low, high = queue.popleft()

            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))

        return True

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

print(result.isValidBST(root))