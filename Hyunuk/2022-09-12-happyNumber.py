class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        while n not in hs:
            hs.add(n)
            n = sum(int(i) ** 2 for i in str(n))
            if n == 1:
                return True
        return False
