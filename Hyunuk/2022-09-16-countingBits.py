class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(num):
            count = 0
            while num > 0:
                num &= num - 1
                count += 1
            return count
        ret = [0] * (n + 1)
        for i in range(n + 1):
            ret[i] = cnt(i)
        return ret
