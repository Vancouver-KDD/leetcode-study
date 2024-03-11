class Solution:
    def rob(self, nums: List[int]) -> int:
        # odd indices or even indices
        # odd = 0
        # even = 0
        # for index in range(len(nums)):
        #     isOdd = index % 2
        #     if not isOdd:
        #         even += nums[index]
        #     else:
        #         odd += nums[index]
        # return max(even,odd)

        first, secondAndMax = 0, 0
        for num in nums:
            tempMax = max(num + first, secondAndMax)
            first = secondAndMax
            secondAndMax = tempMax
        return secondAndMax