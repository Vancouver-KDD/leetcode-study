from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


solution = Solution()
output = solution.minEatingSpeed([1,4,3,2], 9)
print(output)
