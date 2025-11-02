class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        bucket = [[] for _ in range (len(nums) + 1)]

        for key, value in freq.items():
            bucket[value].append(key)
        
        result = []
        for j in range(len(nums), -1, -1):
            if k == len(result):
                return result
            result.extend(bucket[j])
        
        return result