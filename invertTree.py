from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
    
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if not node:
            return None
        node.left, node.right = node.right, node.left
        print(node.left.val)
        print(node.right.val)
        self.invertTreeDFS(node.left)
        self.invertTreeDFS(node.right)
        return root
    
    def invertTreeDFSStack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

        

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

# result.invertTreeDFS(root)
result.invertTreeDFSStack(root)
# result.invertTree(root)

        



