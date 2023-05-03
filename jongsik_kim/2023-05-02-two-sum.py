class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2 or len(nums) > 10 ** 4:
            raise ValueError('Invalid Length')
        if target < -10 ** 9 or target > 10 ** 9:
            raise ValueError('Invalid Value')
        hashmap = {}  # initialize a hashmap
        for i in range(len(nums)):
            if nums[i] < -10 ** 9 or nums[i] > 10 ** 9:
                raise ValueError('Invalid Value')
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            else:
                hashmap[nums[i]] = i
        return []


s = Solution()
lst1 = [2, 7, 11, 15]
lst2 = [3, 2, 4]
lst3 = [3, 3]
print(s.twoSum(lst1, 9))
print(s.twoSum(lst2, 6))
print(s.twoSum(lst3, 6))
