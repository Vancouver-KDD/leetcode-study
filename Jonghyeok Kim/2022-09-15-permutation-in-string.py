class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        # create a dict key is char in s1, value is the number of char appearance
        s1_dict = {}
        for ch in s1:
            if ch not in s1_dict:
                s1_dict[ch] = 1
            else:
                s1_dict[ch] += 1
        
        for idx, ch in enumerate(s2):
            # move window and increase value if it is out of the window
            if idx >= s1_len and s2[idx-s1_len] in s1_dict:
                s1_dict[s2[idx-s1_len]] += 1
            
            # if all values are 0, it means s2 contains a permutation of s1
            if ch in s1_dict:
                s1_dict[ch] -= 1
                
            if all([value == 0 for value in s1_dict.values()]):
                return True
        
        return False