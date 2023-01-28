# Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise
# Anagram: word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# `s` and `t` consist of lowercase English letters

class Solution:
    def create_hash_map(self, s: str) -> dict:
        hash = {}
        for letter in s:
            if letter not in hash:
                hash[letter] = 1
            else:
                hash[letter] += 1
        return hash

    # Solution 1: Hash Map
    def isAnagram(self, s: str, t: str) -> bool:
        # Empty case
        if not s or not t:
            return False

        # length diff
        if len(s) != len(t):
            return False

        # Hash map
        hash_s = self.create_hash_map(s)
        hash_t = self.create_hash_map(t)

        return hash_s == hash_t

    # Solution 2: Sort given strings
    def isAnagram_sort(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


def main():
    s = Solution()
    print(s.isAnagram_sort("", ""))

    print(s.isAnagram_sort("anagram", "nagaram"))

    print(s.isAnagram_sort("rat", "car"))


if __name__ == "__main__":
    main()