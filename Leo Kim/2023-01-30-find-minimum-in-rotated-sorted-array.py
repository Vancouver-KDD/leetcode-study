class Solution:
    def findMin(self, nums: List[int]) -> int:

        ## key point of this algorithm is:
        ## nums[middle] >= nums[left]: serach from right else from left

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[r]

        # TC: logN usual bintree tc

        # return min(sorted(nums)) This is faster... SO FUNNY HAHA