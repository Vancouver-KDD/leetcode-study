def threeSum(nums):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        # if there's duplicate value, skip the index
        if i > 0 and a == nums[i - 1]:
            continue

        L, R = i + 1, len(nums) - 1

        while L < R:
            threeSum = a + nums[L] + nums[R]
            if threeSum > 0:
                R -= 1
            elif threeSum < 0:
                L += 1
            else:
                result.append([a, nums[L], nums[R]])
                # [-2, -2, 0, 0, 2, 2]
                L += 1
                R -= 1
                while nums[L] == nums[L - 1] and L < R:
                    L += 1

    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))