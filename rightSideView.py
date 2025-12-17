from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideViewUsingBFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level[len(level)-1])
        return res
    
    def rightSideViewUsingDFSStack(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root,0)]
        while stack:
            node, depth = stack.pop()
            if depth == len(res):
                res.append(node.val)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return res


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

print(result.rightSideViewUsingBFS(root))
print(result.rightSideViewUsingDFSStack(root))