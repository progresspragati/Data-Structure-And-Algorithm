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
            if node1.val != node2.val:
                return False
            if not node1 or not node2:
                return False
            stack1.append(node1.left)
            stack2.append(node2.left)
            stack1.append(node1.right)
            stack2.append(node2.right)
            
        return True    


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

root1 = TreeNode('1')
nodeA1 = TreeNode('2')
nodeB1 = TreeNode('3')
nodeC1 = TreeNode('4')
nodeD1 = TreeNode('5')
nodeE1 = TreeNode('6')
nodeF1 = TreeNode('7')


root1.left = nodeA1
root1.right = nodeB1

nodeA1.left = nodeC1
nodeA1.right = nodeD1

nodeB1.left = nodeE1
nodeB1.right = nodeF1

print(result.isSameTree(root, root1))

