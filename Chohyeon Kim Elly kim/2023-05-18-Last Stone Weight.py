class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = [-x for x in stones]

        heapq.heapify(maxheap)

        while len(maxheap) > 1 :

            largest = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)

            value = largest - second

            heapq.heappush(maxheap, value)

        res = list(maxheap)

        return -res[0]


        
