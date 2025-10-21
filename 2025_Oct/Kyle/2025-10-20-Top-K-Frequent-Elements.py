# O(N^2)
class Solution(object):
    def topKFrequent(self, nums, k):
        # build list of unique elements (preserving first-seen order)
        seen = set()  # 이미 본 값을 파악하기 위한 set
        unique = []  # 처음 마주한 값을 그 마주한 순서대로 저장할 리스트
        for x in nums:
            if x not in seen:
                seen.add(x)
                unique.append(x)  # 이와 같이 마주한 순서대로 한 번씩만 고유하게 저장함.

        # 각 고유값의 갯수와 그 값 자체를 쌍으로 리스트로 저장
        # freq[i] = [count, value]
        freq = []
        for u in unique:
            c = 0
            for x in nums:
                if x == u:
                    c += 1
            freq.append([c, u])  # 다시 처음부터 하나씩 순회하며 갯수를 새서 저장

        # pick the max count k times without sorting
        res = []
        for _ in range(k):
            max_i = 0
            for i in range(1, len(freq)):
                if freq[i][0] > freq[max_i][0]:
                    max_i = i
            res.append(freq[max_i][1])
            freq[max_i][0] = -1  # mark as used so it won't be picked again

        return res

# O(NlogN)
import heapq

class HeapSolution(object):
    def topKFrequent(self, nums, k):
        # 1) frequency count
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # 2) maintain a size-k min-heap of (count, value)
        heap = []
        for val, cnt in freq.iteritems():  # iteritems() for Python 2
            if len(heap) < k:
                heapq.heappush(heap, (cnt, val))
            else:
                # pushpop is a bit faster: pushes then pops the smallest if needed
                heapq.heappushpop(heap, (cnt, val))

        # 3) extract just the values (order doesn’t matter unless problem requires it)
        return [val for (cnt, val) in heap]


# O(N)
class OptimalSolution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [ [] for i in range(len(nums) + 1)]

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