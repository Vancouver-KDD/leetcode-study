class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_other_char(arr):
            return (r - l + 1) - max(arr)
        if not s:
            return 0
        arr = [0] * 26
        ret = 0
        l = 0
        r = 0
        while r < len(s):
            i = ord(s[r]) - ord("A")
            arr[i] += 1
            while get_other_char(arr) > k:
                l_i = ord(s[l]) - ord("A")
                arr[l_i] -= 1
                l += 1
            ret = max(ret, r-l+1)
            r += 1
        return ret
