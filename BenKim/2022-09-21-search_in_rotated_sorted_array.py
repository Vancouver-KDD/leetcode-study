def searchInRotatedSortedArray(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2


        # 오름차순 내림차순
        # 타겟값보다 큰지 작은지

        # 중간기준 오름차순
        if nums[middle] < nums[right] and nums[right] < target:
            left = middle
        else:
            middle = right