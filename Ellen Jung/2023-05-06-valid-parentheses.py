class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        cur = ''
        next = ''
        bracket_map = {'(' : ')', '[' : ']', '{' : '}'}
        for c in s:
            if c in bracket_map.keys():
                cur = c
                next = bracket_map[c]
            else:
                if c is not next:
                    return False
        return True

def main():
    s = Solution()
    boolean = s.isValid("()")
    print(boolean)


if __name__ == '__main__':
    main()