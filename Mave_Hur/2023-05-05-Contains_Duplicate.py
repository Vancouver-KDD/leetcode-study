class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set();

        for i in nums:
            if i in hashset: # meaning i is duplicate
                return True

            hashset.add(i)

        return False