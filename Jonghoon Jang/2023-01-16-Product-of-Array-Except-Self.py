"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import heapq


class Solution:
    #
    # Time complexity: O(N): traverse elements in the nums list once at most
    # Space complexity: O(1): no extra space except answer list
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product_with_zero = 1
        num_zeros = 0

        # count number of zero and total product of all elements except zero
        for i in range(len(nums)):
            total_product_with_zero *= nums[i]
            if nums[i] == 0:
                num_zeros += 1

        # num of zero > 1: all zeros
        if num_zeros > 1:
            return [0] * len(nums)

        # calculate the prod of all the elements except zero
        total_product_non_zero = 1
        for num in nums:
            if num != 0:
                total_product_non_zero *= num

        answer = []

        for num in nums:
            if num != 0:
                answer.append(int(total_product_with_zero / num))
            else:
                answer.append(total_product_non_zero)
        return answer

    # Time complexity: O(N): traverse elements in the nums list once at most
    # Space complexity: O(1): no extra space except answer list
    def productExceptSelfSimpified(self, nums: list[int]) -> list[int]:
        num_zeros = nums.count(0)  # O(N)

        if num_zeros > 1:
            return [0] * len(nums)

        # total product of all elements except zero
        total_product = 1
        total_product_except_zero = 1
        for num in nums:
            total_product *= num
            if num != 0:
                total_product_except_zero *= num

        answer = []

        for num in nums:
            if num != 0:
                answer.append(int(total_product / num))
            else:
                answer.append(total_product_except_zero)  # case such as [-1,1,0,-3,3]
        return answer


def main():
    s = Solution()

    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelfSimpified([1,2,3,4]))

    print(s.productExceptSelf([-1,1,0,-3,3]))
    print(s.productExceptSelfSimpified([-1,1,0,-3,3]))


if __name__ == "__main__":
    main()
