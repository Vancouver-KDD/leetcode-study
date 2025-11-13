from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = Counter(nums)

        top_k = freq_dict.most_common(k)
        return [a for a, b in top_k]
