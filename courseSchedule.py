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
    
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, prq in prerequisites:
            indegree[prq] += 1
            adj[course].append(prq)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return count == numCourses

    def canFinishUsingDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for course, prq in prerequisites:
            premap[course].append(prq)
        print(premap)
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if premap[course] == []:
                return True
            visiting.add(course)
            for prq in premap[course]:
                if not dfs(prq):
                    return False
            visiting.remove(course)
            premap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    
result = Solution()
print(result.canFinishUsingDfs(10, [[1,4], [9,4], [4,5], [5,8], [2,3], [3,8], [7,3], [4,3]]))



        
