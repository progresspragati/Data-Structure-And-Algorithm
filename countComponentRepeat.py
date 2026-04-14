from collections import deque
from typing import List


class Solution:
    def countComponentsUsingDfs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res

    def countComponentsUsingBfs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            queue = deque([node])
            visit[node] = True
            while queue:
                curr = queue.popleft()
                for nei in adj[curr]:
                    if not visit[nei]:
                        visit[nei] = True
                        queue.append(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res

result = Solution()
print(result.countComponentsUsingBfs(5, [[0,1],[1,2],[3,4]]))