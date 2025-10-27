class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 

        start, end = 0, len(s1)-1
        count_s1 = [0]*26
        count_s2 = [0]*26 
        
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1
            count_s2[ord(s2[i])-ord('a')]+=1

        if count_s1 == count_s2: 
            return True 
            
        end+=1
        while end < len(s2):
            count_s2[ord(s2[end]) - ord('a')]+=1 
            count_s2[ord(s2[start])-ord('a')]-=1
            if count_s1 == count_s2:
                return True 
            start+=1
            end+=1
            

        return False        