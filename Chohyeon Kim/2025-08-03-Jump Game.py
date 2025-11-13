class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(n) time and O(1) space, where n is the size of input array.
        # 0 이 걸리면 무조건 Stop
        # [[1 2 0 100 0 1 1]]
        #
        # [2 0]
        #  c g

        goal = len(nums) - 1
        cur = goal - 1

        while goal > 0 and cur >= 0:

            if nums[cur] + cur >= goal:  # 0 + 4 == 5  , 2 + 0 =
                goal = cur
                cur = goal - 1
            else:
                cur -= 1

        return True if goal == 0 else False
