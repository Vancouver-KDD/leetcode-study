"""
49. Group anagram
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution:
    # 1. hash table
    # Time complexity: O(N * K*logK) : len of strs is N(outer loop) and sort each str N(K * logK)
    # Space complexity: O(NK)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_table = {}

        for str in strs:  # O(N)
            sorted_str = ''.join(sorted(str))  # O(K*logK)
            if sorted_str not in hash_table:
                hash_table[sorted_str] = [str]
            else:
                hash_table[sorted_str].append(str)

        return list(hash_table.values())


def main():
    s = Solution()

    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))



if __name__ == "__main__":
    main()
