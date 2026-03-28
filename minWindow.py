class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count_freq = {}
        t_count_freq = {}
        l = 0
        min_window_substring = [-1,-1]
        window = 0
        resLen = float("infinity")
        if len(t) > len(s) or t == "":
            return ""
        for ch in t:
            t_count_freq[ch] = 1 + t_count_freq.get(ch, 0)
        need_window = len(t_count_freq)
        for r in range(len(s)):
            s_count_freq[s[r]] = 1 + s_count_freq.get(s[r], 0)
            if s[r] in t_count_freq and t_count_freq[s[r]] == s_count_freq[s[r]]:
                window += 1
            while window == need_window:
                if (r-l+1) < resLen:
                    min_window_substring = [l, r]
                    resLen = r - l + 1
                s_count_freq[s[l]] -= 1
                if s[l] in t_count_freq and s_count_freq[s[l]] < t_count_freq[s[l]]:
                    window -= 1
                l += 1
        l, r = min_window_substring
        return s[l:r+1] if resLen != float("infinity") else ""

result = Solution()
print(result.minWindow("OUZODYXAZV", "XYZ")) 




        
