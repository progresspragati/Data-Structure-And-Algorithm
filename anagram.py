class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict_s = dict()
        my_dict_t = dict()
        for x in s:
            if x in my_dict_s:
                my_dict_s[x]+= 1
            else:
                my_dict_s.update({x : 1})
        for x in t:
            if x in my_dict_t:
                my_dict_t[x]+= 1
            else:
                my_dict_t.update({x : 1})
        i = 0
        while i < len(s):
            if s[i] not in my_dict_s:
                return False
            elif s[i] not in my_dict_t:
                return False
            elif my_dict_s[s[i]] != my_dict_t[s[i]]:
                return False
            i+= 1
        return True
    
    def isAnagramUsingSet(self, s:str, t:str) -> bool:
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
    
m = Solution()
print(m.isAnagramUsingSet("hello", "llohe"))
