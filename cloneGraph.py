from collections import deque
from typing import Optional

# Definition for a Node.


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraphUsingDfs(self, node: Optional['Node']) -> Optional['Node']:
        old_new_node = {}
        def dfs(node):
            if node in old_new_node:
                return old_new_node[node]
            new_node = Node(node.val)
            print(f"node:{node.val}")
            old_new_node[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
                print(f"{node.val} neighbors: {neighbor.val}")
            return new_node
        
        return dfs(node) if node else None

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new_node = {}
        old_new_node[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old_new_node:
                    old_new_node[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old_new_node[cur].neighbors.append(old_new_node[neighbor])
                    
        for old, clone in old_new_node.items():
            neighbors = [n.val for n in clone.neighbors]
            print(f"{clone.val} -> {neighbors}")
            
        return old_new_node[node]


result = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2]
node2.neighbors = [node1,node3]
node3.neighbors = [node2]
result.cloneGraph(node1)