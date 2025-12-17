from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderUsingBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res_list = []
        queue = deque()
        queue.append(root)
        
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res_list.append(level)
        return res_list
    
    def levelOrderUsingDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dFS(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dFS(node.left, depth+1)
            dFS(node.right, depth+1)
        dFS(root, 0)
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
print(result.levelOrderUsingBFS(root))
print(result.levelOrderUsingDFS(root))