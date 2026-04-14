from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new = {}
        def dfs(node):
            if node in new:
                return new[node]
            copy = Node(node.val)
            new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        result = dfs(node) if node else None
        print(new)
        return result 
    
    def cloneGraphUsingBfs(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new = {}
        new[node] = Node(node.val)
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in new:
                    new[nei] = Node(node.val)
                    queue.append(nei)
                new[cur].neighbors.append(new[nei])
        return new[node]

result = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2]
node2.neighbors = [node1,node3]
node3.neighbors = [node2]
result.cloneGraphUsingBfs(node1)
