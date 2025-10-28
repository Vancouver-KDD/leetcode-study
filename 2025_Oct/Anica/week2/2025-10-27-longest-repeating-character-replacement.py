class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_so_far = 0 
        start, end = 0, 0 

        while end < len(s):
            count[s[end]]+=1 
            max_occ = max(count.values())
            other_letters = end-start+1-max_occ
            
            while other_letters > k: 
                count[s[start]]-=1
                start+=1 
                max_occ = max(count.values())
                other_letters = end-start+1-max_occ
            max_so_far = max(max_so_far, end-start+1)
            end+=1 

        return max_so_far




            



        
       