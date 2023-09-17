class Solution:
    '''
    Read from bottom to top.
    - order: fourSumStep1, fourSumStep2, fourSumStep3, fourSum

    Step 4:
    Optimize Step 3.

    When we have 2 remaining numbers to pick, use Two sum approach, where run time is O(n)

    Runtime: O(n^(k-1)), where k=4 for 4sum.
    - since two sum method will take O(n), it will be O(n^3) instead of O(n^4)
    Space: O(n)
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(lo, hi, curr_sum, path):
            while lo < hi:
                if nums[lo] + nums[hi] + curr_sum == target:
                    result.append(path + [nums[lo], nums[hi]])
                    while lo + 1 <= hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] + curr_sum > target:
                    hi -= 1
                else:
                    lo += 1

        def dfs(lo, hi, curr_sum, path):
            if k - len(path) == 2:
                two_sum(lo, hi, curr_sum, path)
                return

            while lo <= hi:
                dfs(lo + 1, hi, curr_sum + nums[lo], path + [nums[lo]])
                while (lo + 1 <= hi) and nums[lo] == nums[lo + 1]:
                    lo += 1
                lo += 1

        result = []
        k = 4
        nums.sort()
        dfs(0, len(nums) - 1, 0, [])
        return result

    '''
    Step 3:

    - same as step 2, but only save quadruplet when it sums to target
    - Running this will TLE
    - Runtime O(n^k)
    - Space O(n)
    '''
    def fourSumStep3(self, nums: List[int], target: int) -> List[List[int]]:

        def dfs(lo, hi, curr_sum, path):
            if len(path) == k:
                if curr_sum == target:
                    result.append(path)
                return

            while lo <= hi:
                dfs(lo + 1, hi, curr_sum + nums[lo], path + [nums[lo]])
                while (lo + 1 <= hi) and nums[lo] == nums[lo + 1]:
                    lo += 1
                lo += 1

        result = []
        k = 4
        nums.sort()
        dfs(0, len(nums) - 1, 0, [])
        return result

    '''
    Step 2:  get all combinations quadruplet, but do not double count duplicates

    example 1: 
    nums: [1, 1, 2, 3, 4, 5] k=4
    outputs: [[1,2,3,4], [1,2,3,5], [1,2,4,5], [1,3,4,5], [2,3,4,5]]

    example 2: 
    nums: [1a,1b,1c,1d,1e] // put alphabet next to number to show they are distinct
    output: [[1a,1b,1c,1d]]

    '''
    def fourSumStep2(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(lo, hi, path):
            if len(path) == k:
                result.append(path)
                return

            while lo <= hi:
                dfs(lo + 1, hi, 0, path + [nums[lo]])

                # This is to not double count.
                # This will require arrays to be sorted
                while (lo + 1 <= hi) and nums[lo] == nums[lo + 1]:
                    lo += 1
                lo += 1

        k = 4
        result = []
        nums.sort()
        dfs(0, len(nums) - 1, [])
        return result

    '''
    Step 1. get all combinations of quadruplet, regardless of duplicate 

    example 1: 
    nums: [1, 1, 2, 3, 4, 5] k=4
    outputs: [[1,2,3,4], [1,2,3,5], [1,2,4,5], [1,3,4,5], [2,3,4,5]]

    example 2: 
    nums: [1a,1b,1c,1d,1e] // put alphabet next to number to show they are distinct
    output: [[1a,1b,1c,1d], [1b, 1c, 1d, 1e]......]

    '''
    def fourSumStep1(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(lo, hi, path):
            if len(path) == k:
                result.append(path)
                return

            for i in range(lo, hi + 1):
                # path + [nums[i]] --> passes in a copy of array
                dfs(i + 1, hi, path + [nums[i]])

        result = []
        k = 4
        dfs(0, len(nums) - 1, 0, [])
        return result