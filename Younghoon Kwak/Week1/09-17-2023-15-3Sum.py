def threeSum(nums):
    numLength = len(nums)
    outputs = []
    nums.sort() # Sort the list for Two Pointer Approach
    for currentIndex in range(numLength - 2):
        left = currentIndex + 1; 
        right = numLength - 1;
        while left < right: # Loop through util Left Pointer is smaller than the Right Pointer
            numCurrentIndex = nums[currentIndex]
            numLeft = nums[left] 
            numRight = nums[right]
            sum = numCurrentIndex + numLeft + numRight # Add all the pointers 
            if sum == 0: #Once found, Check whether it's not in the results already and move both the pointers
                if [numCurrentIndex, numLeft, numRight] not in outputs: # Make sure same list of numbers are not already there in the outputs. 
                    outputs.append([nums[currentIndex], nums[left], nums[right]]) 
                left += 1 
                right -=1
            elif numCurrentIndex + numLeft + numRight > 0: # If the sum is greater than 0, let's reduce the number (move the right pointer to left)
                right -= 1
            else: # If the sum is less than 0, let's increase the number (move the left pointer to right)
                left += 1
    # Time Complexity is O(nlogn)    
    return outputs