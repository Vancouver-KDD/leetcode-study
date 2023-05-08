class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_array = []
        t_array = []

        for t_value in t:
            t_array.append(ord(t_value) - 96)

        for s_value in s:
            s_array.append(ord(s_value) - 96)

        if sorted(t_array) == sorted(s_array):
            return True
        else:
            return False


def main(self=None):
    s = "rat"
    t = "car"
    result = Solution.isAnagram(self, s, t)
    print(result)

    s2 = "anagram"
    t2 = "nagaram"
    result2 = Solution.isAnagram(self, s2, t2)
    print(result2)


if __name__ == '__main__':
    main()
