#692.Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = 1+count.get(word,0) 

        heap = []
        for str in count.keys():
            heapq.heappush(heap, (-count[str],str))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res