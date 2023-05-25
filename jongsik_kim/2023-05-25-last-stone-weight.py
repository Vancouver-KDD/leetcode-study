import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [x * (-1) for x in stones]
        heapq.heapify(stones)
        while stones:
            # pop the largest element
            e1 = heapq.heappop(stones)
            if not stones:
                return -e1
            # pop the second-largest element
            e2 = heapq.heappop(stones)
            if e1 != e2:
                heapq.heappush(stones, (e1 - e2))
        return 0


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeight([1]))

# stones = [2, 7, 4, 1, 8, 1]
