from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        l = 0
        for i in range(len(strs)):
            if strs[i] == "*":
                continue
            res.append([])
            res[l].append(strs[i])
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    res[l].append(strs[j])
                    strs[j] = "*"
            l += 1
        return res
    
    def groupAnagramsUsingHashMap(self, strs: List[str]) -> List[List[str]]:
        res = {}
        result = []
        for word in strs:
            key = tuple(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        for key, value in res.items():
            result.append(value)
        return result
    
    def groupAnagramsUsingHashMap1(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())

    def groupAnagramsUsingDict(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-97] += 1
            res[tuple(count)].append(word)
        return list(res.values())
        


    
result = Solution()
# print(result.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(result.groupAnagramsUsingDict(["act","pots","tops","cat","stop","hat"]))
# print(result.groupAnagramsUsingHashMap1(["act","pots","tops","cat","stop","hat"]))


        