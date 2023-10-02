class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #still need to working on it
        counter=[]
        total=[]
        pointer = s[0]
        count=0
        index=0

        for i in range(len(s)):
            # print(s[i])
            if s[i] == pointer:
                count+=1
                index+=1
            else:
                if count >= k:
                    counter.append(count)
                pointer = s[i]
                count = 1
                index+=1
        
        if len(counter) == 0 and index == len(s):
            return 0
        return index-k+1