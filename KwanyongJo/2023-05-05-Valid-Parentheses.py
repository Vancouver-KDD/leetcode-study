# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # count = 0
        while len(s) > 0:
            length_s = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            # print(s)
            # count += 1
            # print(count)
            if length_s == len(s):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("([]){}"))
