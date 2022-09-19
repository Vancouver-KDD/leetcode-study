from typing import List

## Sort method Time: O(nlogn) Space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

## Hashmap method.  Time: O(n) Space: O(n)
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return True
            hashmap.add(n)

class Solution3:
    def containsDuplicate(selfself, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
