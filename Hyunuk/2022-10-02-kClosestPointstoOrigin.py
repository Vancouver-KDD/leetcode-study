import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for x, y in points:
            dist = (y ** 2) + (x ** 2)
            heapq.heappush(hq, (dist, x, y))
        ret = []
        while k > 0:
            dist, x, y = heapq.heappop(hq)
            ret.append([x, y])
            k -= 1
        return ret
