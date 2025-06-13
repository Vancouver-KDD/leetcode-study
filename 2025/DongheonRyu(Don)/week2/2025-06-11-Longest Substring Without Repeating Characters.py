def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = 0 
        max_len = 0

        for i,val in enumerate(s):
            
            if val in map and map[val] >=start:
               start = map[val] +1
            map[val] = i
            max_len = max(max_len,i-start +1)
        return max_len