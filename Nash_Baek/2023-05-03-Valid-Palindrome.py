# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/476

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Error handling part
        # The length of string should be from 1 to 2*10^5.
        # It requires O(1) time complexity.
        if not (1 <= len(s) <= 2 * 10**5 ):
            raise ValueError("Out of the string length")

        # Removing non-alphanumeric characters from string
        # Using isalnum, join, filter function
        # It requires O(N) time complexity.
        s = ''.join(filter(lambda str: str.isalnum(), s))

        # Converting all letters to lower case
        # After that, reverse the string
        # It requires O(N) time complexity.
        s = s.lower()
        s_reverse = s[::-1]

        # Comparing the original string with reversed string.
        # The overall time complexity is O(N) and space complexity is O(1)
        return s == s_reverse

# solution = Solution()
# str = "abC!c Ba!#"
# print(solution.isPalindrome(str))