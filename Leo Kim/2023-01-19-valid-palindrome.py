class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        s = s.lower()

        for i in s:
            if i.isalnum():
                ans += i

        return ans == ans[::-1]

        ## simple O(n)