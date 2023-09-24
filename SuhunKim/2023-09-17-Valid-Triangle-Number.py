class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # ### Approach 1 (Brute force), O(n^3) => TLE at test case 223 ###
        # combinations = itertools.combinations(nums, 3)
        # res = 0
        
        # for combination in combinations:
        #     temp = list(sorted(combination))
        #     if temp[0]+temp[1] > temp[2]:
        #         res += 1
        # return res
    
        # ### Approach 2 (sort first, hash), O(n^3)###
        # nums.sort()
        # res = 0
        # dictionary = {}
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         short_sides_sum = nums[i]+nums[j]
        #         if short_sides_sum in dictionary:
        #             dictionary[short_sides_sum].append((i,j))
        #         else:
        #             dictionary[short_sides_sum] =[(i,j)]

        # for short_sides_sum in dictionary:
        #     for indices in dictionary[short_sides_sum]:
        #         i, j = indices
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] > nums[k]:
        #                 res += 1
        # return res
    
        # ## Approach 3 (sort, two pointers), O(n^3) => TLE at 224 ###
        # nums.sort()
        # res = 0
        
        # for mid in range(1, len(nums)-1):
        #     for left in range(mid-1,-1,-1):
        #         flag = False
        #         for right in range(mid+1,len(nums)):
        #             if nums[left]+nums[mid] > nums[right]:
        #                 res += 1
        #             else:
        #                 break
        #                 flag = True
        #         if flag: break
        # return res
    
        ### Approach 4 (sort, two pointers, improved) ###
        nums.sort()
        res = 0
        
        for right in range(len(nums)-1, 1, -1):
            left, mid = 0, right-1
            while (left < mid):
                if nums[left] + nums[mid] > nums[right]:
                    res += mid-left
                    mid -= 1
                else:
                    left += 1
        return res
        