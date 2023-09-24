
class Solution:
    def threeSumClosest(self, nums, target):
        N = len(nums)
        nums.sort()
        # If there are only three items in the list, just return the sum of three integers
        if N == 3:
            return sum(nums)
        # Define the minSum and minDiffrence
        minSum, minDiff = None, float('inf')
        for i in range(N-2):
            # Skip the same integer
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Definte left and right 
            left, right = i+1, N-1
            # Loop until left < right 
            while left < right: 
                currSum = sum([nums[i], nums[left], nums[right]]) # Get the sum
                currDiff = abs(target - currSum) # Get Difference from the Target 
                if currDiff < minDiff: # If the difference is smaller than min difference calcuated then change minDiff to currDifference
                    minDiff = currDiff
                    minSum = currSum # Sum will be the result 
                    if minDiff == 0: # If target == the difference, then return the code 
                        print(minSum)
                        return minSum
                if target > currSum: # If target is still bigger, increase the number so that there will be a smaller difference (Incrase the left pointer)
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else: # If target is still less, decrease the number so that there will be a smaller difference (Decrease the right pointer)
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        # All traverses, return the minSum that's closed target.
        return minSum