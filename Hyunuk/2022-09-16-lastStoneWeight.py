import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ret = []
        for stone in stones:
            heapq.heappush(ret, (-stone, stone))
        while len(ret) > 1:
            first_stone = heapq.heappop(ret)[1]
            second_stone = heapq.heappop(ret)[1]
            if first_stone > second_stone:
                stone = first_stone - second_stone
                heapq.heappush(ret, (-stone, stone))
        return sum(i[1] for i in ret)
    