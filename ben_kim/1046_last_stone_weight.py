class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] # 1
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = abs(heapq.heappop(stones))
            s2 = abs(heapq.heappop(stones))
            if s1 != s2:
                heapq.heappush(stones, -abs(s1 - s2))
        
        return abs(stones[0]) if len(stones) else 0
        
# 1. heapq module implements a min heap, but you can implement a max heap by negating the values before adding them to the heap and negating them again when extracting the maximum value