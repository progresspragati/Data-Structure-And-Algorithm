from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        strs = []
        def dfs(node):
            nonlocal strs
            if not node:
                strs.append("N")
                return
            strs.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(strs)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split(",")
        self.i = 0
        def dFS():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dFS()
            node.right = dFS()
            return node
        return dFS()
        
result = Codec()
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

strs = result.serialize(root)
print(strs)
print(result.deserialize(strs))