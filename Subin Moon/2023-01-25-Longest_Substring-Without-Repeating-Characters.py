# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    # Solution 1: Two pointers  O(n)?
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 1
        left = 0
        right = 1

        while left <= right < len(s):
            length = right - left + 1

            if s[right] not in s[left:right]:
                right += 1
                res = max(res, length)

            else:
                left += 1
                right = left + 1

        return res

    # Solution 2: Brute Force  O(n^3)
    def lengthOfLongestSubstring_bf(self, s):
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

    # Solution 3: Sliding window  O(n)
    def lengthOfLongestSubstring_sliding_window(self, s):
        from collections import Counter
        chars = Counter()
        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res

    # Solution 4: Sliding window optimized  O(n)
    def lengthOfLongestSubstring_sliding_window_opt(self, s):
        n = len(s)
        ans = 0
        mp = {} # Stores the current index of a char
        i = 0

        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans

    # Solution 5: Using ASCII table to optimize space complexity to O(m) when m is the size of charset
    def lengthOfLongestSubstring_space(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res