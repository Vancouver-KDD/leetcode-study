"""
Longest Repeating Substring With Replacement

You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements,
return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1
Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

python3 Hye/week2/2024-10-w2-longest-repeating-substring-with-replacement.py
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Iterate through the string and count the number of letters
        2. Update the max_length
        3. if the length is greater than the max count + k, update left and reduce count (shrink window)
        """
        counter = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_length = max(max_length, counter[s[right]])

            if right - left + 1 > max_length + k:  # max length doesn't have to be s[right]
                counter[s[left]] -= 1
                left += 1
        
        return right - left + 1


def main():
    sol = Solution()
    print("Week 2: Longest Repeating Substring With Replacement")
    s = "XYYX"
    k = 2
    expected_output = 4
    print(f"\nExample 1: s = {s}, k = {k}, expected output: {expected_output}")
    output = sol.characterReplacement(s, k)
    assert output == expected_output
    
    s = "AAABABB"
    k = 1
    expected_output = 5
    print(f"\nExample 2: s = {s}, k = {k}, expected output: {expected_output}")
    output = sol.characterReplacement(s, k)
    assert output == expected_output
    

if __name__ == "__main__":
    main()
