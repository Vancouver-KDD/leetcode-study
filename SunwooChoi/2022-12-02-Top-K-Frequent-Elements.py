from heapq import * 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = self.get_counter(nums)
        heap = []
        
        for key in counts:
            heappush(heap, [-counts[key], key])
        
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        
        return res
    
    def get_counter(self, nums: List[int]) -> Dict[int, int]:
        result = {}
        for el in nums:
            result[el] = result[el] + 1 if el in result else 1
        return result

