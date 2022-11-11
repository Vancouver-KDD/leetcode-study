class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # track frequecies in substring
        freq_dict = {}
        # max frequencies in substring
        max_freq = 0
        left, right = 0, 0
        result = 0
        
        while right < len(s):
            freq_dict[s[right]] = freq_dict[s[right]] + 1 if s[right] in freq_dict else 1
            max_freq = max(max_freq, freq_dict[s[right]])
            
            # if substring is not valid, shrink the size of substring
            if k < right - left + 1 - max_freq:
                freq_dict[s[left]] -= 1
                left += 1
                
            result = max(result, right-left+1)
            right += 1  
        
        return result
    
