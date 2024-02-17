class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. You can change each uppercase English character to any other uppercase English character N times. (max N time)
        2. Find the longest substing that consists of the same characters after perform changing characters. 
        
        Strategy
        - Sliding window
        How
        - using hashmap to store characters
        - condition is t - m <= k
            - t = size of the window
            - m = the count of the most frequency character
            - k = the given number that allows you to change character
        - keep adding characters to hashmap until condition is false
        - If condition is false, then move the left pointer to the right and check condition again.
        
        """
        hashMap = {}
        left = 0
        res = 0
        
        for right in range(len(s)):
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)
            
            while (right - left + 1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res