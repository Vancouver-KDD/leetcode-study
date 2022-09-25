class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nlogn sort
        nums.sort()
        res = []
        for idx, n in enumerate(nums):
            # if elem is duplicate, skip the loop to prevent duplicate triplets
            if idx > 0 and n == nums[idx-1]:
                continue
            hash_map = {}
            # nums[i] is fixed. we need to find nums[j] + nums[k] = -nums[i]
            for nested_idx in range(idx+1, len(nums)):
                
                if nums[nested_idx] not in hash_map:
                    hash_map[-1*n-nums[nested_idx]] = nums[nested_idx]
                else:
                    if len(res) > 0 and res[-1][-1] == nums[nested_idx] and res[-1][-2] == hash_map[nums[nested_idx]]:
                        continue
                    res.append([n, hash_map[nums[nested_idx]], nums[nested_idx]])
        return res
