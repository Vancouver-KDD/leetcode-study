"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.

python3 Hye/week2/2024-10-w2-longest-substring-without-duplicates.py
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. Iterate through the string
        2. update the left index when duplicate is found
        3. update the max length
        """
        seen = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


def main():
    sol = Solution()
    print("Week 2: Longest Substring Without Duplicates")
    
    s = "zxyzxyz"
    expected_output = 3
    print(f"\nExample 1: s = {s}, expected output: {expected_output}")
    output = sol.lengthOfLongestSubstring(s)
    print(output == expected_output)

    s = "xxxx"
    expected_output = 1
    print(f"\nExample 2: s = {s}, expected output: {expected_output}")
    output = sol.lengthOfLongestSubstring(s)
    print(output == expected_output)
    

if __name__ == "__main__":
    main()
