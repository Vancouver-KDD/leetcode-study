# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/474

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Put the error handling code in here
        # 1. Check the length of strings, 1 <= strings < 5 * 10**4
        if not (1 <= len(s) < 5 * 10**4 and 1 <= len(t) < 5 * 10**4):
            raise ValueError("The length of string is not valid.")

        # 2. Check the elements of strings. Only contains lowercase English letters using ASCII code.

        chars_s = list(s)
        chars_t = list(t)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if any(element not in alphabet for element in chars_s + chars_t):
            raise ValueError("Out of bound")

        # Comparing two strings
        # Step 1. comparing the length of both strings
        # It requires O(N), N is max(len(s), len(t))
        if len(s) != len(t):
            return False

        # Step 1-1. Counting the number of occurrence letters from the string s
        # Matching the ASCII code number - 97 to the index of list variable
        # For example, s = "abca", count_s[0] = 2, count_s[1] = 1, count_s[2] = 1
        # It requires O(N), N is length of s
        count_s_list=[0] * ((ord('z') - ord('a')) + 1)
        count_t_list=[0] * ((ord('z') - ord('a')) + 1)

        for element in chars_s:
            count_s_list[ord(element) - ord('a')] += 1

        print('#' * 10)
        # Step 1-2. Counting the number of occurrence letters from the string t
        # Matching the ASCII code number - 97 to the index of list variable
        # For example, t = "abca", count_t[0] = 2, count_t[1] = 1, count_t[2] = 1
        # It requires O(N), N is length of s

        for element in chars_t:
            count_t_list[ord(element) - ord('a')] += 1

        # Step 1-3. comparing two lists and returns the result.
        if count_s_list == count_t_list:
            return True
        else:
            return False