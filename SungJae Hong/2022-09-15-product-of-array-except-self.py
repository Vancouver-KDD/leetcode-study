from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Returning this list
        answer = [1] * len(nums)
        #Prefix and postfix both have to start at 1 because theres no prefix and postfix for first and last index.
        prefix = 1
        #Getting the multiplied value from the left side of the given index.
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #Getting the multiplied value from the right side of the given index.
        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
