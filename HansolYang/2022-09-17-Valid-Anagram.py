class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if not(s[i] in dic.keys()):
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for i in range(len(t)):
            if not(t[i] in dic.keys()) or dic[t[i]] == 0:
                return False
            else:
                dic[t[i]] -= 1
        
        return True
        