class Solution(object):
    def isPalindrome(self, s):

        convert_list = []

        for c in s:

            if c.isalnum():
                convert_list.append(c.lower())

        print(convert_list)

        l = 0
        r = len(convert_list) - 1

        while l < r:
            if convert_list[r] != convert_list[l]:
                return False

            l += 1
            r -= 1

        return True
