class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen: set
        # left = 0, max_len = 0
        # iterate through the arr s with pointer right
        # if s[right] is not in the set seen, add s[right] into set seen and update max_len = max(curr_len, max_len), go to next
        # if s[right] is in the set seen, iterate with while loop until s[left] == s[right], each iteration remove s[left] from the set seen
        # return max_len

        seen = set()
        left = 0
        max_len = 0

        for right, curr in enumerate(s):
            if curr in seen:
                while curr in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(curr)
            max_len = max(max_len, right - left + 1)
        return max_len
