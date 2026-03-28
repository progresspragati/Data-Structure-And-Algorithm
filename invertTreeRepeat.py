from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode]):
            if not node:
                return None
            temp = node.left
            node.left = node.right
            node.right = temp
            dfs(node.left)
            dfs(node.right)
        cur = root
        dfs(cur)
        return root
    def invertTreeUsingBfs(self, root: Optional[TreeNode])-> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
    
    def invertTreeUsingDfsIterate(self, root:Optional[TreeNode])-> Optional[TreeNode]:
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
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4, None, None)
node5 = TreeNode(5, None, None)
node6 = TreeNode(6, None, None)
node7 = TreeNode(7, None, None)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
root = result.invertTreeUsingDfsIterate(node1)
def preOrder(root:Optional[TreeNode]):
    if not root:
        return None
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def bfs(root:Optional[TreeNode]):
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
# preOrder(root)
bfs(root)



