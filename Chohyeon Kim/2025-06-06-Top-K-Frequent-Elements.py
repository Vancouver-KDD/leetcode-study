class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_buckets = list()
        for _ in range(len(nums)):
            freq_buckets.append(set())

        freq_map = dict()
        for num in nums:
            if num in freq_map:
                freq_buckets[freq_map[num]].remove(num)
                freq_map[num] += 1
                freq_buckets[freq_map[num]].add(num)
            else:
                freq_buckets[0].add(num)
                freq_map[num] = 0

        result = list()
        print(freq_buckets)
        for bucket in reversed(freq_buckets):
            for val in bucket:
                if len(result) != k:
                    result.append(val)
                else:
                    return result
        return result
