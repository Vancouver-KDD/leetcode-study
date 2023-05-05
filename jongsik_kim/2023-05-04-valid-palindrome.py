class Solution:
    # time complexity: O(n)
    # space complexity: O(n^2?)
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1 or len(s) > 2 * 10**5:
            raise ValueError('Invalid Length')
        if len(s.strip()) == 0:
            return True
        strs = ""
        for i in s:
            if i.isalnum():
                strs = ''.join((strs, i.lower()))
        print(strs, len(strs))
        for i in range(len(strs) // 2):
            print(strs[i], strs[-i - 1])
            if strs[i] != strs[-i - 1]:
                return False
        return True


s = Solution()
print(s.isPalindrome(str(input())))
