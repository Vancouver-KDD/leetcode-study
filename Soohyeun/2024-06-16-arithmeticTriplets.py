class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_triplets = 0
        set_nums = set(nums) # O(n)

        for num in nums:
            if (num + diff) in set_nums and (num + diff + diff) in set_nums:
                num_triplets += 1
            
        return num_triplets
