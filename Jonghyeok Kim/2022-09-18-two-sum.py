class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        # key: taget-element / value: element
        for idx, n in enumerate(nums):
            if n not in hash_map:
                hash_map[target-n] = idx
            else:
                # if n in is the map, target - n + n = target.
                # Thus, [n,target-n] is the answer
                return [hash_map[n], idx]