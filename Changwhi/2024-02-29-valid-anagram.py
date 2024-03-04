class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1, string2 = [0] * 26, [0] * 26
        
        if len(s) != len(t):
            return False
        
        for index in range(len(s)):
            string1[ord(s[index]) - ord("a")] += 1 
            string2[ord(t[index]) - ord("a")] += 1
        
        return string1 == string2