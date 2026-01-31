from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]
        for course, prq in prerequisites:
            indegree[prq] += 1
            adj_list[course].append(prq)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
    
result = Solution()
print(result.canFinish(2, [[0,1], [1,0]]))



        
