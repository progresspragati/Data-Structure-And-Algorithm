from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack1.append(node1.left)
            stack2.append(node2.left)
            stack1.append(node1.right)
            stack2.append(node2.right)
            
        return True    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

result = Solution()
root = TreeNode('1')
nodeA = TreeNode('2')
nodeB = TreeNode('3')
nodeC = TreeNode('4')
nodeD = TreeNode('5')
nodeE = TreeNode('6')
nodeF = TreeNode('7')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

root1 = TreeNode('2')
nodeA1 = TreeNode('4')
nodeB1 = TreeNode('5')

root1.left = nodeA1
root1.right = nodeB1

print(result.isSubtree(root, root1))