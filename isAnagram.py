class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashset = {}
        t_hashset = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_hashset:
                s_hashset[s[i]] = 1
            else:
                s_hashset[s[i]] += 1
            if t[i] not in t_hashset:
                t_hashset[t[i]] = 1
            else:
                t_hashset[t[i]] += 1
        if len(s_hashset) != len(t_hashset):
            return False
        for char in s_hashset:
            if char not in t_hashset or s_hashset[char] != t_hashset[char]:
                return False
        return True
    
    def isAnagramUsingSingleHashSet(self, s: str, t: str) -> bool:
        s_hashset = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_hashset:
                s_hashset[s[i]] = 1
            else:
                s_hashset[s[i]] += 1
            if t[i] in s_hashset:
                s_hashset[t[i]] -= 1
            else:
                s_hashset[t[i]] = -1
        for char in s_hashset:
            if s_hashset[char] != 0:
                return False
        return True
    
    def isAnagramOptimum(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashset = {}
        for char in s:
            s_hashset[char] = s_hashset.get(char, 0)+1
        for char in t:
            if char not in s_hashset:
                return False
            s_hashset[char] -= 1
            if s_hashset[char] < 0:
                return False
        return True
    def isAnagramUsingList(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for char in s:
            count[ord(char)-97] += 1
        for char in t:
            count[ord(char)-97] -= 1
            if(count[ord(char)-97]) < 0:
                return False
        return True
        

result = Solution()
print(result.isAnagramUsingList("racecar", "carrace"))