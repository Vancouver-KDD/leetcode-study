from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        answer = []

        # index: frequency, value: list of numbers with that frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # iterate from high to low frequency to find k most frequent elements
        for bucket in reversed(buckets):
            for n in bucket:
                answer.append(n)
                if len(answer) == k:
                    return answer