class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * l
        postfix = [1] * l

        for index in range(l):
            if index == 0:
                prefix[index] = nums[index]
                postfix[l-1] = nums[l-1]
            else:
                prefix[index] = prefix[index-1] * nums[index]
                postfix[l-1-index] = postfix[l-index] * nums[l - 1 -index]

        res = []
        for index in range(l):
            if index == 0:
                res.append(postfix[1])
            elif index == l-1:
                res.append(prefix[index-1])
            else:
                res.append(prefix[index - 1] * postfix[index + 1])

        return res