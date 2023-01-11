"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution:
    # 1. Use Hash table
    # Time complexity: O(n) : maximum n times of search and add to dictionary
    #                         for dictionary, search and add have O(1) T-complexity
    # Space complexity: O(n) : hash table is linear with n
    def containDuplicate(self, nums: list[int]) -> bool:
        nums_map = {}
        contain_duplicate = False
        for num in nums:
            if num in nums_map:
                return True
            else:
                nums_map[num] = 1
        return contain_duplicate

    # 2. Set
    # Time: O(n) : set is implemented as a hash table
    # Space: O(n) : same with a hash table
    def containDuplicateSet(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


def main():
    s = Solution()

    print(s.containDuplicate([1, 2, 3, 1]))
    print(s.containDuplicateSet([1, 2, 3, 1]))

    print(s.containDuplicate([1, 2, 3, 4]))
    print(s.containDuplicateSet([1, 2, 3, 4]))

    print(s.containDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(s.containDuplicateSet([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    main()
