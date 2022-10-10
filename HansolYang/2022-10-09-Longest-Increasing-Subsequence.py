class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        arr = [1] * n
 
        # Compute optimized LIS values in bottom up manner
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and arr[i] < arr[j] + 1:
                    arr[i] = arr[j]+1
 
        # Initialize maximum to 0 to get
        # the maximum of all LIS
        maximum = 0
 
        # Pick maximum of all LIS values
        for i in range(n):
            maximum = max(maximum, arr[i])
 
        return maximum