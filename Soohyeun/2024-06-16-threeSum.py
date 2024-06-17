class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort (nlogn)
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2): # len(nums) > 3
            if i == 0 or nums[i] != nums[i-1]: # Avoid duplicates
                left_point = i + 1
                right_point = len(nums) - 1
                while left_point < right_point:
                    if nums[left_point] + nums[right_point] == -(nums[i]):
                        triplets.append([nums[i], nums[left_point], nums[right_point]])
                        left_point += 1
                        right_point -= 1
                        while left_point < right_point and nums[left_point] == nums[left_point-1]:
                            left_point += 1
                    elif nums[left_point] + nums[right_point] > -(nums[i]): # make it smaller
                        right_point -= 1
                    else: # make is bigger
                        left_point += 1
        return triplets