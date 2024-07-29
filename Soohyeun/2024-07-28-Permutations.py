class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1
        # 2 1 / 1 2
        # 3 2 1 / 2 3 1 / 2 1 3/ 3 1 2 / 1 3 2/ 1 2 3
        subarrays = [[nums[0]]]

        for j in range(1, len(nums)):
            temp_res = []
            for subarray in subarrays:
                n = len(subarray) + 1
                for i in range(n):
                    copied_subarray = subarray[:]
                    copied_subarray.insert(i, nums[j])
                    temp_res.append(copied_subarray)
            subarrays = temp_res
        return subarrays
