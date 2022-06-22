class Solution:
    def findMin(self, nums: List[int]) -> int:

        ## key point of this algorithm is:
        ## nums[middle] >= nums[left]: serach from right else from left

        f = 0
        l = len(nums) - 1

        while f <= l:
            mid = (f + l) // 2
            if nums[mid] < nums[l]:
                l = mid
            else:
                f = mid + 1 # move to the + 1 right

        return nums[l]

    ## this solution only care the right array divided by middle
    ## is this optimal?