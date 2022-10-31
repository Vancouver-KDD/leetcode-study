class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(n, h):
            counter = 0
            for pile in piles:
                counter += math.ceil(pile/n)
                if counter > h:
                    return False
            return True

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            middle = (l + r) // 2
            # if middle is possible, check the left to find the smaller case
            if can_finish(middle, h):
                res = min(res, middle)
                r = middle - 1
            else:
                l = middle + 1
        return res
