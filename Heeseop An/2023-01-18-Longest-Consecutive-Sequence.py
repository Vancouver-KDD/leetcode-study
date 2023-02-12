class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) # O(n)
        longest = 0

        for num in numsSet: # O(n)
            if num - 1 not in numsSet:
                curr = num
                currLongest = 1

                while curr + 1 in numsSet: # O(1)
                    curr += 1
                    currLongest += 1

                longest = max(longest, currLongest)

        return longest