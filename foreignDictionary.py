from collections import deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {ch:set() for w in words for ch in w }
        indegree = {c: 0 for c in adj_list}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            if (len(word1) > len(word2)) and (word1[:min_len] == word2[:min_len]):
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        print(indegree)
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj_list[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) != len(indegree):
            return ""
        return "".join(res)
    
    def foreignDictionaryUsingDfs(self, words: List[str]) -> str:
        adj_list = {ch:set() for w in words for ch in w }
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for neighbor in adj_list[char]:
                if dfs(neighbor):
                    return True
                
            visited[char] = False
            res.append(char)
        
        for char in adj_list:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)



result = Solution()
print(result.foreignDictionaryUsingDfs(["hrn","hrf","er","enn","rfnn"]))