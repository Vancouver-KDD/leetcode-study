from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        minim = nums[0]
        for i in range(len(nums)):
            if nums[i] > minim:
                answer = max(answer, nums[i] - minim)
            minim = min(minim, nums[i])
        return answer