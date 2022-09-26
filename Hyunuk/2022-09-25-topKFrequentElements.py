class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        cnt = collections.Counter(nums)
        for i in cnt:
            bucket[cnt[i]].append(i)
        ret = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                ret.append(j)
                if len(ret) == k:
                    return ret
