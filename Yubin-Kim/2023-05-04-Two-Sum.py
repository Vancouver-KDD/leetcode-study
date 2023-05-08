class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLength = len(nums)
        for i in range(0, numsLength):
            for j in range(i + 1, numsLength):
                numsSum = nums[i] + nums[j]
                if numsSum == target:
                    result = [i, j]
                    return result
                else:
                    continue


def main(self=None):
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution.twoSum(self, nums, target)
    print(result)

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = Solution.twoSum(self, nums2, target2)
    print(result2)

    nums3 = [3, 3]
    target3 = 6
    result3 = Solution.twoSum(self, nums3, target3)
    print(result3)


if __name__ == '__main__':
    main()