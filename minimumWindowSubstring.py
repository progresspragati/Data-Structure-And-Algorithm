class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) and t == "":
            return ""
        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        res = [-1,-1]
        reslen = float("infinity")
        for i in range(len(s)):
            count_s = {}
            for j in range(i, len(s)):
                count_s[s[j]] = 1 + count_s.get(s[j], 0)

                flag = True
                for c in count_t:
                    if count_t[c] > count_s.get(c, 0):
                        flag = False
                        break
                
                if flag and (j - i + 1) < reslen:
                    reslen = j -i + 1
                    res = [i, j]

        return s[res[0] : res[1]+1] if reslen != float("infinity") else "" 
    
    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t) and t == "":
            return ""
        count_t = {}
        window = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have = 0
        need = len(count_t)
        res = [-1, -1]
        reslen = float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        return s[res[0] : res[1]+1] if reslen != float("infinity") else "" 



        
result = Solution()
print(result.minWindow("OUZODYXAZV", "XYZ"))
print(result.minWindow2("OUZODYXAZV", "XYZ"))
        
