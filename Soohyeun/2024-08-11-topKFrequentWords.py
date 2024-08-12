class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1

        heap = []
        for word, num in words_dict.items():
            heapq.heappush(heap, (-num, word))

        res = []
        for _ in range(k):
            curr = heapq.heappop(heap)
            res.append(curr[1])

        return res
