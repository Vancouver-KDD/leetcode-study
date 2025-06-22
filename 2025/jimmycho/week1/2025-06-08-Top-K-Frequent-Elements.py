from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_count = Counter(nums)
        return [num for num, count in nums_count.most_common(k)]