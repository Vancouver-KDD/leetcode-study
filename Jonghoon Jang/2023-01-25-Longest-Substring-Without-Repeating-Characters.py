"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring without repeating characters.
"""


class Solution:
    # Sliding window
    # Time complexity: O(n): worst case 2n
    # Space complexity: O(m): to store the longest sub-string
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        l, r = 0, 1
        longest_subs = s[l]
        curr_subs = s[l]
        # sliding window
        while r < len(s):
            # unique char
            if s[r] not in curr_subs:
                curr_subs += s[r]
                if len(curr_subs) > len(longest_subs):
                    longest_subs = curr_subs
                r += 1
            # duplicate char, then move left pointer
            else:
                l += 1
                r = l + 1
                curr_subs = s[l]
        return len(longest_subs)

    # Sliding window
    # Time complexity: O(n): r iterate n times
    # Space complexity: O(min(m, n)): min(m, n)
    def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res



def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstringOptimized("abcabcbb"))

    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstringOptimized("bbbbb"))

    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstringOptimized("pwwkew"))


if __name__ == "__main__":
    main()
