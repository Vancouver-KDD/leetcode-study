import math


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


def main(self=None):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = Solution.search(self, nums, target)
    print(result)

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = Solution.search(self, nums2, target2)
    print(result2)


if __name__ == '__main__':
    main()
