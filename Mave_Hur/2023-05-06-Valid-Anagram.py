class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        # why dictionary??
        # look up in constant time

        # store char and # of its appearance
        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1

        # check the other string using the dictionary
        for char in t:
            if char not in dict:
                return False
            dict[char] -= 1

        for frequency in dict.values():
            if frequency != 0:
                return False
        return True

        # time complexity?? o(n_1 + n_2)
        # bc wdk which one is bigger so add them up.

        # space complexity?? o(n_1)
        # bc only one dictionary is needed.
