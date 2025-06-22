class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        left = 0

        answer = 0

        for right in range(len(s)):
            
            while s[right] in window:
                window.remove(s[left])
                left = left + 1

            window.add(s[right])
            answer = max(answer, right - left + 1)
        
        return answer
        