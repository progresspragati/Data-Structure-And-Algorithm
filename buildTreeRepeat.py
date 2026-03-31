from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
    
    def buildTreeUsingHashDfs(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        def dfs(l,r):
            nonlocal pre_idx
            if l>r:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)
    
    def buildTreeUsingHashDfsOptimal(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0
        in_index = 0
        def dfs(limit):
            nonlocal pre_index, in_index
            if pre_index >= len(preorder):
                return None
            if inorder[in_index] == limit:
                in_index += 1
                return None
            root = TreeNode(preorder[pre_index])
            pre_index += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float("inf"))




