class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'(': ')', '{': '}', '[': ']'}
        new_string = []

        for char in s:
            if char in mapping:
                new_string.append(char)
            elif new_string and mapping[new_string[-1]] == char:
                new_string.pop()
            else:
                return False

        return not new_string


def main(self=None):
    s = "()"
    result = Solution.isValid(self, s)
    print(result)

    s2 = "()[]{}"
    result2 = Solution.isValid(self, s2)
    print(result2)

    s3 = "(]"
    result3 = Solution.isValid(self, s3)
    print(result3)


if __name__ == "__main__":
    main()
