# Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct

# Input: nums = [1, 2, 3, 1]
# Output: true

# Input: nums = [1, 2, 3, 4]
# Output: false

# Input: nums= [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

class Solution:
    # Solution 1: Brute Force
    def containDuplicate(self, nums: list[int]) -> bool:
        pointer = 0
        result = False
        while not result:
            if nums[pointer] in nums[pointer + 1:]:
                result = True
                break
            else:
                pointer += 1
                if pointer == len(nums):
                    break
        return result

        # Solution 2: Hash Table

    def containDuplicateHashTable(self, nums: list[int]) -> bool:
        hash_tab = {}
        for i in nums:
            if i not in hash_tab:
                hash_tab[i] = 1
            else:
                hash_tab[i] += 1

        for i in hash_tab:
            if hash_tab[i] > 1:
                return True
        return False

    # Solution 3: Sorting
    def containDuplicateSorting(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


def main():
    s = Solution()

    print(s.containDuplicate([1, 2, 3, 1]))
    print(s.containDuplicateHashTable([1, 2, 3, 1]))
    print(s.containDuplicateSorting([1, 2, 3, 1]))

    print(s.containDuplicate([1, 2, 3, 4]))
    print(s.containDuplicateHashTable([1, 2, 3, 4]))
    print(s.containDuplicateSorting([1, 2, 3, 4]))

    print(s.containDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(s.containDuplicateHashTable([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(s.containDuplicateSorting([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    main()
