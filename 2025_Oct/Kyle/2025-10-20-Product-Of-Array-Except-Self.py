
# O(N^2)
class Solution(object):
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        for i in range(len(nums)):
            left = 1
            right = 1
            for j in range(i):
                left *= nums[j]
            for j in range(i + 1, len(nums)):
                right *= nums[j]
            output[i] = left * right

        return output

# O(N)
class BetterSolution(object):
    def productExceptSelf(self, nums):
        left_multiples = [1] * len(nums)
        right_multiples = [1] * len(nums)
        final_output = [1] * len(nums)

        for i in range(1, len(nums)):
            left_multiples[i] = nums[i - 1] * left_multiples[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_multiples[i] = nums[i + 1] * right_multiples[i + 1]

        for i in range(len(nums)):
            final_output[i] = left_multiples[i] * right_multiples[i]

        return final_output


# O(N) O(1)

class OptimalSolution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer


