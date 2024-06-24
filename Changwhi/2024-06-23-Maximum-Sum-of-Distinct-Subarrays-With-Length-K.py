class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        checkDuplicate = set()
        l, res, temp = 0, 0, 0

        for i in range(len(nums)):
            #instantiate and assgin value to avoid key error
            while r in checkDuplicate or (r - l + 1) > k:
                temp -= nums[l]
                checkDuplicate.remove(nums[l])
                temp -= nums[l]
                l += 1
            temp += nums[r]
            checkDuplicate.add(nums[r])
            if (r - l +1) === k:
                res = max(res, temp)
    return res 

            

