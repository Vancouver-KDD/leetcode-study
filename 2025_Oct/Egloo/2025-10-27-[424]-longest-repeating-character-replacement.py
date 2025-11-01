from collections import deque 

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        azSet = [chr(i) for i in range(ord('A'), ord('Z'))]
        maxLen = 0
        for r in azSet:
            q = deque()
            q.append(0)

            for i in range(len(s)):
                if r != s[i]:
                    q.append(i+1)
                    if len(q) > k + 1:
                        leftmost = q.popleft()
                        curLen = i - leftmost

                        if curLen > maxLen: 
                            maxLen = curLen
            curLen = len(s) - q[0]
            if curLen > maxLen:
                maxLen = curLen
        return maxLen