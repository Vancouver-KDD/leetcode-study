"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution:
    # 1. Counter using hash table
    # Time complexity: O(n) : maximum n times of search and add to dictionary
    #                         for dictionary, search and add have O(1) T-complexity
    # Space complexity: O(n) : hash table is linear with n
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:  # both empty string
            return True

        if len(s) != len(t):
            return False

        char_dict = {}  # Frequency Counter
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False
            else:
                char_dict[char] -= 1

        # Check if the count for every character is zero
        for value in char_dict.values():
            if value != 0:
                return False

        return True

    # 2. User sort
    # Time complexity: O(n*logn): python sort() has time complexity of O(n*logn)
    # Space complexity: O(n) : creates two new lists of size n and also performs comparison of
    #                          both lists which also has a O(n) space complexity
    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


def main():
    s = Solution()

    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagramSort("anagram", "nagaram"))

    print(s.isAnagramSort("rat", "car"))
    print(s.isAnagram("rat", "car"))


if __name__ == "__main__":
    main()
