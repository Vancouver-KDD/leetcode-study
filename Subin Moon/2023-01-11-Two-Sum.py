"""
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""

class Solution:
    # Solution 1: Brute Force
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

        # Empty list
        if not nums:
            return result

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)

        return result

    # Solution 2: less than O(n^2) time complexity? (i.e. without two loops)
    def twoSum_faster(self, nums: list[int], target: int) -> list[int]:
        hash = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [i, hash[diff]]
            hash[nums[i]] = i
        return []


def main():
    s = Solution()
    print(s.twoSum([], 10))
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))

    print(s.twoSum_faster([2, 7, 11, 15], 9))
    print(s.twoSum_faster([3, 2, 4], 6))
    print(s.twoSum_faster([3, 3], 6))


if __name__ == "__main__":
    main()
