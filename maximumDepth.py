from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
    
    def maxDepthUsingStack(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        stack = [[root,depth]]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return maxDepth
    
    def maxDepthUsingBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        maxDepth = 0
        while queue:
            node, depth = queue.popleft()
            maxDepth = max(maxDepth, depth)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return maxDepth



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

# print(result.maxDepth(root))
# print(result.maxDepthUsingStack(root))
print(result.maxDepthUsingBFS(root))