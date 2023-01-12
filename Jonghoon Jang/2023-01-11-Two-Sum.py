"""
1. Two Sum
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    # 1. hash table
    # Time complexity: O(n) : loop through n elements twice.
    #                         for dictionary, lookup and add have O(1), constant
    # Space complexity: O(n) : extra space for hash table that is linear with n
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}  # key: complement (target - num), value: index of number
        for i in range(len(nums)):
            # check if the complement exists
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]

            diff = target - nums[i]
            if diff not in dictionary:
                dictionary[diff] = i

    # 2. Optimized brute force using sort
    # Time complexity: O(n^2): python sort() has time complexity of O(n*logn)
    # Space complexity: O(1) : not depend on the size. constant
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)  # sort O(n*logn)
        for i in range(len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                if sorted_nums[j] == target - sorted_nums[i]:  # basic operation O(n^2)
                    first = nums.index(sorted_nums[j])
                    second = nums.index(sorted_nums[i])
                    if first != second:
                        return [first, second]
                    else:  # find the 2nd index of the duplicate num e.i [3, 3]
                        return [first, nums.index(sorted_nums[i], first + 1)]


def main():
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSumBruteForce([2, 7, 11, 15], 9))

    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSumBruteForce([3, 2, 4], 6))

    print(s.twoSum([3, 3], 6))
    print(s.twoSumBruteForce([3, 3], 6))


if __name__ == "__main__":
    main()
