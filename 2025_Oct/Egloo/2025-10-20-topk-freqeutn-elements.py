import heapq 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

        h = []

        for key in dic:
            if len(h) < k:
                heapq.heappush(h, (dic[key], key))
            else:
                if h[0][0] < dic[key]:
                    heapq.heappop(h)
                    heapq.heappush(h, (dic[key], key))

        return [v[1] for v in h]
