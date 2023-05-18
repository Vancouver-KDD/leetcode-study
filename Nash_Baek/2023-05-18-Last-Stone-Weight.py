# https://leetcode.com/problems/last-stone-weight/

import heapq

# First of all, find the heaviest two stones from the list by using max_heap
class Heap:

    # Pop and compare
    # Push the result. The result will be empty if x == y, else the result will be y-x
    # Iterate the loop until the number of elements is 1 or 0
    # Return the value of element. If there are no elements left, it will return 0
    def last_stone_weight(self, stones: list[int]) -> int:
        max_heap = [-element for element in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(max_heap, stone1 - stone2)
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0

list = [2, 7, 4, 1, 8, 1]
heap = Heap()
print(heap.last_stone_weight(list))
