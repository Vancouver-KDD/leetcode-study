from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)

        left = 0

        answer = 0

        for right in range(len(s)):

            freq[s[right]] += 1

            maxFreq = max(freq.values())
            currentLength = right - left + 1

            if currentLength - maxFreq > k:
                freq[s[left]] -= 1
                left = left + 1
                currentLength = right - left + 1
            
            answer = max(answer, currentLength)

        return answer
        
        