from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i = 0
        j = 0
        n = len(preorder)
        while i < n  and j < n:
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right = curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1
        return head.right
    
result = Solution()
nodeA = TreeNode(2)
nodeB = TreeNode(1)
nodeC = TreeNode(3)
nodeA.left = nodeB
nodeA.right = nodeC
print(result.kthSmallest(nodeA, 1))
head = result.buildTree([1,2,3,4], [2,1,3,4])
queue = deque([head])
while queue:
    node = queue.popleft()
    print(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
