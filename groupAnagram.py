from typing import List

class Solution:
    def isAnagramUsingSet(self, s:str, t:str) -> bool:
        if s == None or t == None:
            return False
        if len(s) != len(t):
            return False
        list_s = [0]*26
        list_t = [0]*26
        i = 0
        while i < len(s):
            list_s[ord(s[i]) - ord("a")] += 1
            list_t[ord(t[i]) - ord("a")] += 1
            i += 1
        j = 0
        while j < len(list_s):
            if list_s[j] != list_t[j]:
                return False
            j += 1
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = []
        i = 0
        while i < len(strs):
            if(strs[i] == None):
                i += 1
                continue
            j = i + 1
            subList = []
            subList.append(strs[i])
            while j < len(strs):
                if self.isAnagramUsingSet(strs[i], strs[j]):
                    subList.append(strs[j])
                    strs[j] = None
                j += 1
            group_anagram.append(subList)
            i += 1
        return group_anagram
                
result = Solution()
print(result.groupAnagrams(["act","pots","tops","cat","stop","hat"]))