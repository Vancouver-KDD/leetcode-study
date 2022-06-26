class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = max(a, b)
        for i in range(abs(min(a, b))):
            if (min(a, b)) < 0:
                res -=1
            else:
                res += 1
        return res