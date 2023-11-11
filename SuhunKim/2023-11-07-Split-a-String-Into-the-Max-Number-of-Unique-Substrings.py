class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(added, s):
            if len(s) == 0:
                return len(added)
            
            temp = ""
            res = 0
            for i in range(len(s)):
                temp += s[i]
                if temp not in added:
                    added.add(temp)
                    res = max(res, helper(added, s[i+1:]))
                    added.remove(temp)
            return res
        
        return helper(set(), s)