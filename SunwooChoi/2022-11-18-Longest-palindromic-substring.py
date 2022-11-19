class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        # if there is one or zero, return itself
        if size <= 1:
            return s
        
        max_sub = s[0]
        for i in range(size):
            # get longest palidrome with one element
            solo = self.get_longest_pali(i,i,s)
            # get longest palidrome with two elements
            neighor = self.get_longest_pali(i,i+1,s)
            # update max palindromic substring
            if len(solo) > len(max_sub):
                max_sub = solo
            if len(neighor) > len(max_sub):
                max_sub = neighor
        return max_sub
    
    def get_longest_pali(self, left: int, right: int, s: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

