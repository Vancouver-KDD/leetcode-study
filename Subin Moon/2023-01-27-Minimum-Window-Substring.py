"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
from collections import Counter


class Solution:
    # Solution 1: time and space complexity - O(|S| + |T|) where |S| and |T| are length of strings S and T respectively
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)  # num of unique characters in t, which need to be present in the desired window

        l, r = 0, 0  # pointers

        # used to keep track of how many unique characters in t are present in the current window in its desired frequency
        # e.g. t="AABC" -> window must have two As, one B and one C -> formed=3
        formed = 0

        window_counts = {}
        ans = float("inf"), None, None  # ans tuple of the form (window length, left, right)

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1  # get(a, 0): return 0 when a doesn't exist

            # If the frequency fo the current char added equals to the desired count in t, increase the formed
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'
            while 1 <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the 'left' pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


    # Solution 2: Optimized sliding window
    def minWindow_2(self, s, t):
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        # Filter all the chars from s into a new list along with their index
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            if window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = filtered_s[l][1]

                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]