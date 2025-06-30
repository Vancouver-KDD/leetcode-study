def search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right)//2
        if nums[middle] > nums[right]:
            left = middle+1
        else:
            right=middle
    min_index=left
    if min_index==0:
        left, right=0, n-1
    elif target >= nums[0] and target <= nums[min_index-1]:
        left, right = 0, min_index - 1
    else:
        left, right = min_index, n - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left=middle+1
        else:
            right=middle-1
    return -1
        


print(search([4, 5, 6, 7, 0, 1, 2], target = 0))
