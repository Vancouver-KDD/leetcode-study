class Solution:
    def reverse(self, x: int) -> int:
        min_ = -2 ** 31
        max_ = (2 ** 31) - 1
        is_neg = (x < 0)
        s = str(x)
        num = int(s[-1])
        ret = (num * -1) if is_neg else num
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "-":
                continue
            num = int(s[i]) * -1 if is_neg else int(s[i])
            if ret > max_ // 10 or (ret == max_ // 10 and num > 7):
                return 0
            elif ret < (min_ // 10) + 1 or (ret == min_ // 10 + 1) and num > 8:
                return 0
            ret = (ret * 10) + num
        return ret

