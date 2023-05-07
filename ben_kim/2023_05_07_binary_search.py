def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1 # 1
        else:
            r = mid - 1
    
    return -1

# 1. Since mid is different from target, it moves one more pointer.