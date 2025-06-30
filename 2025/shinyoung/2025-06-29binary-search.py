def search(nums, target):
    def dfs(left, right):
        middle = left + (right - left) // 2
        if right-left < 1:
            if nums[left] == target:
                return middle
            else:
                return -1
        if target == nums[middle]:
            return middle
        if target < nums[middle]:
            return dfs(left, middle-1)
        if target > nums[middle]:
            return dfs(middle+1, right)
    return dfs(0, len(nums)-1)


# print(search([-1, 0, 3, 5, 9, 12], target=9))
# print(search([-1, 0, 3, 5, 9, 12], target=2))
print(search([5], target=5))
print(search([2, 5], target=0))
