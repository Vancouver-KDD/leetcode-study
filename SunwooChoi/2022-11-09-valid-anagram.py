class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_dict, t_dict = {}, {}
        for c in s:
            c_dict[c] = 1 + c_dict[c] if c in c_dict else 1
        
        for c in t:
            t_dict[c] = 1 + t_dict[c] if c in t_dict else 1

        return t_dict == c_dict

