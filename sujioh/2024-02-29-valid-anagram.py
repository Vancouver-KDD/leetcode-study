from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)

        for char in t:
            counter[char] -= 1

        for c in counter:
            if counter[c] != 0:
                return False

        return True
