from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        for i in range(len(words)-1):
            w1 = words[i] 
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minLen] == w2[: minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []
        def dfs(ch):
            if ch in visited:
                return visited[ch]
            visited[ch] = True
            for neighchar in adj[ch]:
                if dfs(neighchar):
                    return True
            visited[ch] = False
            res.append(ch)

        for ch in adj:
            if dfs(ch):
                return ""
        res.reverse()
        return "".join(res)

result = Solution()
print(result.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))


