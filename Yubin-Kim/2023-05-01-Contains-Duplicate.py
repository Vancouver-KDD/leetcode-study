class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = list(set(nums))
        numsLength = len(nums)
        resultLength = len(result)
        if resultLength == numsLength:
            return False
        else:
            return True

def main(self=None):
    nums = [1, 2, 3, 1]
    result = Solution.containsDuplicate(self, nums)
    print(result)

    nums2 = [1, 2, 3, 4]
    result2 = Solution.containsDuplicate(self, nums2)
    print(result2)

    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = Solution.containsDuplicate(self, nums3)
    print(result3)


if __name__ == '__main__':
    main()
