# nums = [1,2,3,1]

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums1 = nums[1:] # [2,3,1]
        nums2 = nums[:-1] #[1,2,3]

        dp1 = [nums1[0], max(nums1[0], nums1[1])]
        dp2 = [nums2[0], max(nums2[0], nums2[1])]

        # 2,3
        for i in range(2, len(nums1)):
            exclude = dp1[i-1]
            include = dp1[i-2] + nums1[i]
            val = max(exclude, include)
            dp1.append(val)

        for j in range(2, len(nums2)):
            exclude = dp2[j-1]
            include = dp2[j-2] + nums2[j]
            val = max(exclude, include)
            dp2.append(val)

        print(dp1)
        print(dp2)
        return max(dp1[-1], dp2[-1])
