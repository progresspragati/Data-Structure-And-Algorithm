from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSameTree(node, subRoot) == True:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    
    def isSameTree(self, root: Optional[TreeNode], subRoot:Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        stack = [[root, subRoot]]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if (not node1 or not node2 or node1.val != node2.val):
                return False
            stack.append([node1.left, node2.left])
            stack.append([node1.right, node2.right])
        return True


                
                


        