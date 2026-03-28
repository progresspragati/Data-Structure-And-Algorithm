from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack = [[p,q]]
        while stack:
            node1, node2 = stack.pop()
            if node1.val != node2.val:
                return False
            if node1.left and node2.left:
                stack.append([node1.left, node2.left])
            if node1.right and node2.right:
                stack.append([node1.right, node2.right])
            elif (node1.left and not node1.left) or (not node1.left and node2.left):
                return False
            elif (node1.right and not node1.right) or (not node1.right and node2.right):
                return False
        return True

            