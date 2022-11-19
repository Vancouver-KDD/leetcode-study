class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        result = 0

        for i in range(size):
            result += self.get_num_palindromes(i,i,s)
            result += self.get_num_palindromes(i,i+1,s)
        return result

    def get_num_palindromes(self, left: int, right: int, s: str) -> int:
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result

