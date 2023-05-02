class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) < 1 or len(nums) > 10**5:
            # check the length
            raise TypeError('Invalid length')
        nums_set = set()
        for i in nums:
            if i < -10**9 or i > 10**9:
                # check the value
                raise ValueError('Invalid value')
            if i in nums_set:
                return True
            nums_set.add(i)
        return False


s = Solution()
input1 = [1, 2, 3, 1]
input2 = [1, 2, 3, 4]
input3 = [1, 1, 1, 3, 3, 4, 5, 4, 2, 4, 2]
input4 = []
input5 = [-10**10]
print(s.containsDuplicate(input1))
print(s.containsDuplicate(input2))
print(s.containsDuplicate(input3))
# print(s.containsDuplicate(input4))
# print(s.containsDuplicate(input5))

