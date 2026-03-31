from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node:Optional[TreeNode], depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            print(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res
    
    def levelOrderUsingBFS(self, root: Optional[TreeNode])-> List[List[int]]:
        res = []
        queue = deque([root])
        while queue:
            lenQ = len(queue)
            level = []
            for i in range(lenQ):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res


result = Solution()
root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(3)
nodeC = TreeNode(4)
nodeD = TreeNode(5)
nodeE = TreeNode(6)
nodeF = TreeNode(7)

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF
            
print(result.levelOrderUsingBFS(root))
            