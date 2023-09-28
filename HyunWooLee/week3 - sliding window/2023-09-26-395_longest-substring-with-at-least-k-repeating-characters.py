class Solution:
    '''
    sliding window template
    - always move right first

    lo, hi = 0, 0
    while hi < len(input):
        # do something (usually if statement)
        # right += 1

        # do something (usually either if or while statement)
        # left += 1

    - question: why iterative from 1 to len of unique chars?
    --> because we do not easily know window shrinking criteria
    - see below.

     - let k = 3

     ex1) z z z t t
     unique 1 : z z z
     unique 2 : None satisfy


     ex2) z z z t t k k k
     unique 1: z z z OR k k k
     unique 2: None
     unique 3: None

     ex3)  z z z t t k k k t
     unique1: z z z or k k k
     unique 2: t t k k k t
     unique 3: None


     runtime: O(n)
      - for each distinct lower case (at most 26), do sliding window.
     space: O(n)
      - all strings can be unique
    '''
    def longestSubstring(self, s: str, k: int) -> int:
        unique_chars_len = len(set(s))
        result = 0

        for i in range(1, unique_chars_len + 1):
            unique_chars = 0
            at_least_k = 0
            window = {}

            left, right = 0, 0
            while right < len(s):
                curr_right = s[right]

                if curr_right not in window:
                    window[curr_right] = 0
                    unique_chars += 1

                window[curr_right] += 1
                if window[curr_right] == k:
                    at_least_k += 1

                if unique_chars == i and at_least_k == i:
                    result = max(result, right - left + 1)

                right += 1

                while len(window) > i:
                    curr_left = s[left]
                    window[curr_left] -= 1
                    if window[curr_left] == k - 1:
                        at_least_k -= 1
                    if window[curr_left] == 0:
                        del window[curr_left]
                        unique_chars -= 1
                    left += 1
        return result
