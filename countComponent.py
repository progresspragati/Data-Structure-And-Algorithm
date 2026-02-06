from collections import deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visit = [False]*n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for neighbor in adj_list[cur]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        q.append(neighbor)
        number_of_graph = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                number_of_graph += 1
        return number_of_graph   
    
    def countComponentsUsingDfs(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            for neighbor in adj_list[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
        res = 0
        
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res



result = Solution()
print(result.countComponentsUsingDfs(5, [[0,1],[1,2],[3,4]]))         
