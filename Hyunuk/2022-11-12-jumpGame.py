class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt = nums[0]
        for i in range(1, len(nums)):
            if cnt == 0:
                return False
            cnt -= 1
            cnt = max(cnt, nums[i])
            
        return True
