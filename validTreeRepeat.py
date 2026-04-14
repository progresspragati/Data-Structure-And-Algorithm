from collections import deque
from typing import List


class Solution:
    def validTreeUsingDfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        print(adj)
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and len(visit) == n

    def validTreeUsingBfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = deque([(0,-1)])
        visit = set()
        visit.add(0)
        while queue:
            node, par = queue.popleft()
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add((nei))
                queue.append((nei, node))
        return len(visit) == n
                
result = Solution()
print(result.validTreeUsingBfs(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
