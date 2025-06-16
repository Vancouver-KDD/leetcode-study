from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = defaultdict(int)

        for num in nums:
            ans[num] += 1

        temp = []
        for num, cnt in ans.items():
            temp.append([cnt, num])
        temp.sort()

        res = []
        while len(res) < k:
            res.append(temp.pop()[1])

        return res
    
class Solution2: #better efficient solution
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = dict()
        freq = [ [] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res