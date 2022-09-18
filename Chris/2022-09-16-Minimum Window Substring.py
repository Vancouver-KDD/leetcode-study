class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        
        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        # need = number of characters in countT
        # have = number of characters matching frequency with chars in countT
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        
        
        l = 0
        # keep moving right pointer to the right until the end
        # once meeting the condition, adjust left pointer to minimize the size of the window
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:

                if (r - l +1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                #adjust left pointer to minimize the window size
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r =res
        return s[l:r+1] if resLen != float("infinity") else ""
                
        
        
        
        
        
        
        