# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()  # e.g. Counter({'A': 3, 'B': 2})
        for right in range(1, len(s) + 1):  # right = [1, len(s) + 1]
            counts[s[right - 1]] += 1  # count chars
            max_char_n = counts.most_common(1)[0][1]  # Get the num of the most common character

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left


s = Solution()
print(s.characterReplacement("AABABBA", 1))