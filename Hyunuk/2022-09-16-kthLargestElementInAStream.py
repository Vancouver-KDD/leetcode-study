import heapq

class KthLargest:
    
    def _pop(self):
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)


    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        heapq.heapify(self.arr)
        self._pop()
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        self._pop()
        return self.arr[0]
