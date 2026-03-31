from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("+inf"))])
        while queue:
            node, left, right = queue.popleft()
            if not(left < node.val < right):
                return False
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))
        return True

    def isValidBSTUsingDfs(self, root: Optional[TreeNode]) -> bool:
        def isValid(node:Optional[TreeNode], left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root, float("-inf"), float("inf"))

result = Solution()
nodeA = TreeNode(0)
nodeB = TreeNode(1)
nodeC = TreeNode(3)
nodeA.left = nodeB
nodeA.right = nodeC
print(result.isValidBSTUsingDfs(nodeA))
            
