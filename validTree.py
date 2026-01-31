from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        adj_list = [[] for _ in range(n)]
        for vertex1, vertex2 in edges:
            adj_list[vertex1].append(vertex2)
            adj_list[vertex2].append(vertex1)
        
        visit = set()
        q = deque([(0,-1)])
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in visit:
                    return False
                visit.add(neighbor)
                q.append((neighbor, node))

        return len(visit) == n

result = Solution()
print(result.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))