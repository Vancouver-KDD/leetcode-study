import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = r"[^0-9a-zA-Z]"
        new_string = re.sub(pattern, "", s)
        result_string = new_string.lower()
        string_length = len(result_string)
        middle_index = int(round(string_length / 2))
        string_start = []
        string_end = []

        for i in range(0, middle_index):
            string_start.append(result_string[i])

        if string_length % 2 != 0:
            for j in range(string_length - 1, middle_index, -1):
                string_end.append(result_string[j])
        else:
            for j in range(string_length - 1, middle_index - 1, -1):
                string_end.append(result_string[j])

        if string_start == string_end:
            return True


def main(self=None):
    s = "A man, a plan, a canal: Panama"
    result = Solution.isPalindrome(self, s)
    print(result)

    s2 = "race a car"
    result2 = Solution.isPalindrome(self, s2)
    print(result2)

    s3 = " "
    result3 = Solution.isPalindrome(self, s3)
    print(result3)

    s4 = "0P"
    result4 = Solution.isPalindrome(self, s4)
    print(result4)

    s5 = "a"
    result5 = Solution.isPalindrome(self, s5)
    print(result5)


if __name__ == '__main__':
    main()