def findKthLargest(nums, k):
    def partition(left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    left = 0
    right = len(nums) - 1
    k -= 1

    while left <= right:
        pivot_index = partition(left, right)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
