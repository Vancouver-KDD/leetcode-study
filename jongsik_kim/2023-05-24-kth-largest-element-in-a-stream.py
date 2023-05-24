import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.arr = nums
        self.k = k
        self.heap = []
        for i in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, i)
            else:
                if self.heap[0] < i:
                    heapq.heappushpop(self.heap, i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if self.heap[0] < val:
                heapq.heappushpop(self.heap, val)
        return self.heap[0]

        # TRY_1
        # self.arr = nums
        # self.k = k
        # self.heap = []
        # for i in self.arr:
        #     if len(self.heap) < k:
        #         heapq.heappush(self.heap, i)
        #     else:
        #         if self.heap[0] < i:
        #             heapq.heappushpop(self.heap, i)
        #             heapq.heapify(self.heap)

        # TRY_1
        # self.arr += [val]
        # for i in self.arr:
        #     if len(self.heap) < self.k:
        #         heapq.heappush(self.heap, i)
        #     else:
        #         if self.heap[0] < i:
        #             heapq.heappushpop(self.heap, i)
        #             heapq.heapify(self.heap)
        # print(self.heap)
        # return self.heap[0]


k = KthLargest(3, [4, 5, 8, 2])
print(k.add(3))
print(k.add(5))
print(k.add(10))
print(k.add(9))
print(k.add(4))

k2 = KthLargest(1, [])
print(k2.add(-3))
print(k2.add(-2))
print(k2.add(-4))
print(k2.add(0))
print(k2.add(4))
