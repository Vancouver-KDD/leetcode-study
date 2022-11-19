class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        # if there is one or zero, return itself
        if size <= 1:
            return size

        result = 0
        for i in range(size):
            # get longest palidrome with one element
            solo = self.get_longest_pali(i,i,s)
            # get longest palidrome with two elements
            neighor = self.get_longest_pali(i,i+1,s)
            result += solo
            result += neighor
        return result

    def get_longest_pali(self, left: int, right: int, s: str) -> int:
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result

