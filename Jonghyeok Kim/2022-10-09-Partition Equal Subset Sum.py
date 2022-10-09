class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            tmp_dp = set()
            for s in dp:
                if s + nums[i] == target:
                    return True
                tmp_dp.add(s + nums[i])
                tmp_dp.add(s)
            dp = tmp_dp
        return False

        