class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sChars = {}
        tChars = {}

        for i in range(len(s)):
            currentSValue = sChars.get(s[i], 0)
            sChars[s[i]] = currentSValue + 1

            currentTvalue = tChars.get(t[i], 0)
            tChars[t[i]] = currentTvalue + 1

        return sChars == tChars