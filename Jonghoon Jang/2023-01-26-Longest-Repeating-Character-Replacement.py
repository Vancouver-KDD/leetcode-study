"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change
 it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing
the above operations.
"""


class Solution:
    # Sliding window
    # Time complexity: O(n): single pass at most once
    # Space complexity: O(m): to store uppercase so m = 26
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0

        l = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            if (r - l + 1) - max_freq > k:  # window size - max freq > k.  AABBBA 5 - 3 > 2
                count[s[l]] -= 1  # shrink window size and move l pointer to the right
                l += 1

            ans = max(ans, r - l + 1)
        return ans


def main():
    s = Solution()
    str = "ABAB"
    k = 2
    print(s.characterReplacement(str, k))


if __name__ == "__main__":
    main()
