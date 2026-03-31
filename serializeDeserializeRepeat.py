from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def dfsPreorder(root):
            nonlocal data
            if not root:
                data.append("N")
                return
            data.append(str(root.val))
            dfsPreorder(root.left)
            dfsPreorder(root.right)
        dfsPreorder(root)
        return "#".join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("#")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        if not root:
            return "N"
        queue = deque([root])
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

result = Codec()
node1 = TreeNode(-15)
node2 = TreeNode(10)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(-5, None, None)
node6 = TreeNode(5, None, None)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node6
node4.left = node5
data = result.serialize(node1)
head = result.deserialize(data)
def dfs(root):
    if not root:
        return None
    print(root.val)
    dfs(root.left)
    dfs(root.right)
dfs(head)
            
            
            
        

