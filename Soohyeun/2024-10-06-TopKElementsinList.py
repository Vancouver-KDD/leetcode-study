class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        nums_heap = []
        for num, num_of_num in nums_dict.items():
            heapq.heappush(nums_heap, (-num_of_num, num))

        res = []
        for _ in range(k):
            num, curr_num = heapq.heappop(nums_heap)
            res.append(curr_num)

        return res