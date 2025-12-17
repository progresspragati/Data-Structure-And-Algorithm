from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def stackNodes(self, root):
        stack = [root]
        nodes = []
        while stack:
            node =stack.pop()
            nodes.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return nodes
        
    def maxPathSumBruteForce(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        list_nodes = self.stackNodes(root)
        max_sum = -float('inf')
        for start in list_nodes:
            stack = [(start, start.val)]
            while stack:
                node, cur_sum = stack.pop()
                max_sum = max(max_sum, cur_sum)
                if node.left:
                    stack.append((node.left, cur_sum + node.left.val))
                if node.right:
                    stack.append((node.right, cur_sum + node.right.val))
        return max_sum
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dFS(root):
            nonlocal res
            if not root:
                return 0
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, root.val + left + right)
            dFS(root.left)
            dFS(root.right)
        dFS(root)
        return res

    def getMax(self, root)-> int:
        if not root:
            return 0
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        path = root.val + max(left, right)
        return max(0, path)

result = Solution()
root = TreeNode(-15)
nodeA = TreeNode(10)
nodeB = TreeNode(20)
nodeC = TreeNode(15)
nodeD = TreeNode(5)
nodeE = TreeNode(-5)

root.left = nodeA
root.right = nodeB

nodeB.left = nodeC
nodeB.right = nodeD
nodeC.left = nodeE

print(result.maxPathSum(root))
print(result.maxPathSumBruteForce(root))