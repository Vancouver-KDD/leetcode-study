class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ### Approach 1 (brute force with combinations): TLE at test cases 51 ###
        ### O(N^3) ###
        # combinations = itertools.combinations(nums, 3)
        # diff = 10**4*2
        # res = 0
        # for com in combinations:
        #     if diff > abs(sum(com) - target):
        #         diff = abs(sum(com) - target)
        #         res = sum(com)
        # return res
        
        ### Approach 2 (using dictionary with double iteration): TLE at  test cases 81 ###
        ### O(3*N^2) ###
        # d = {}
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if j < len(nums)-1:
        #             d[nums[i]+nums[j]] = nums[:i] + nums[i+1:j] + nums[j+1:]
        #         else:
        #             d[nums[i]+nums[j]] = nums[:i] + nums[i+1:j]
        # res = 0
        # diff = 10**4*2
        # for two_sum in d:
        #     for third_element in d[two_sum]:
        #         three_sum = two_sum + third_element
        #         if diff > abs(three_sum - target):
        #             diff = abs(three_sum - target)
        #             res = three_sum
        # return res
        
        ### Approach 3 (with dictionary, more optimized from second; save picked indicies) : TLE all test cases passed, but took too long ###
        # d = {}
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         d[nums[i]+nums[j]] = (i, j)
        # res = 0
        # diff = 10**4*2
        # for two_sum in d:
        #     for i in range(len(nums)):
        #         if i not in d[two_sum]:
        #             three_sum = two_sum + nums[i]
        #             if diff > abs(three_sum - target):
        #                 diff = abs(three_sum - target)
        #                 res = three_sum
        # return res
        
        ### Approach 4 (sorted array, two pointers, with average midpoint) ###
        # nums.sort()
        # mid,  diff = 0, 10**4*2
        # for i in range(1, len(nums)-1):
        #     if diff >= abs(sum(nums[i-1:i+2]) - target):
        #         diff = abs(sum(nums[i-1:i+2]) - target)
        #         mid = i
        # print(nums)
        # print(mid, nums[mid], target)
        # diff = 10**4*2
        # left, right = mid-1, mid+1
        # while left >= 0 and right <= len(nums)-1:
        #     temp_sum = nums[left]+nums[mid]+nums[right]
        #     if abs(temp_sum - target) < diff:
        #         res = temp_sum
        #         diff = abs(temp_sum - target)
        #     if temp_sum < target:
        #         right += 1
        #     elif temp_sum > target:
        #         left -= 1
        #     else:
        #         return temp_sum
        # return res
    
        ### Approach 5 (sorted array, two pointers, iteration for midpoint) ###
        nums.sort()
        mid, diff = 0, 10**4*2
        for mid in range(1, len(nums)):
            left, right = mid-1, mid+1
            while left >= 0 and right <= len(nums)-1:
                temp_sum = nums[left]+nums[mid]+nums[right]
                if abs(temp_sum - target) < diff:
                    res = temp_sum
                    diff = abs(temp_sum - target)
                if temp_sum < target:
                    right += 1
                elif temp_sum > target:
                    left -= 1
                else:
                    return temp_sum
        return res