class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # to use a min heap as a max heap, multiply -1 to all stone values
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        
        while(len(stones) > 1):
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            if stone1 != stone2:
                heapq.heappush(stones, -abs(stone1 - stone2))
        
        return -stones[0] if len(stones) > 0 else 0
        