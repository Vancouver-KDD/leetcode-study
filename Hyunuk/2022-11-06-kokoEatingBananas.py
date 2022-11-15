class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_eatable(m):
            cnt = 0
            for pile in piles:
                cnt += pile // m
                if pile % m:
                    cnt += 1
                if cnt > h:
                    return False
            return True
            
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if is_eatable(m):
                r = m - 1
            else:
                l = m + 1
        return l
