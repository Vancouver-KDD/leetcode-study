class Solution:
    def permute(self, num):
        res = [[]]
        for n in num:
            size = len(res)
            for _ in range(size):
                r = res.pop(0)
                for i in range(len(r) + 1):
                    t = r[:]
                    t.insert(i, n)
                    res.append(t)
        return res
