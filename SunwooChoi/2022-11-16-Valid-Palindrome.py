class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = self.clean_up(s)
        left, right = 0, len(clean_str) - 1
        
        # compare characters with same distance from center
        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
    # clean up string
    def clean_up(self, s: str) -> str:
        low = s.lower() # convert to lower case
        result = re.sub(r'[^a-z0-9]','', low) # delete non-alpha chars
        return result

