class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        out = filter(str.isalnum, s)
        out_list = list(out)
        for i in range(int(len(out_list)/2)):
            if out_list[i] != out_list[-i-1]:
                return False
        return True