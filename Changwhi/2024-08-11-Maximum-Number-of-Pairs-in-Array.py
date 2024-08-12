class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cache = defaultdict(int)
        pairs = 0

        for num in nums:
            cache[num] += 1

            if cache[num] % 2 == 0:
                pairs += 1        

        return [pairs, len(nums) - pairs * 2]