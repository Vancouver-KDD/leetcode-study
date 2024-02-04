# 424. Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
#
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        start = 0
        max_length = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_freq = max(max_freq, count[s[end]])

            if (end - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

# Example usage
sol = Solution()
print(sol.characterReplacement("ABAB", 2))  # Output: 4
print(sol.characterReplacement("AABABBA", 1))  # Output: 4