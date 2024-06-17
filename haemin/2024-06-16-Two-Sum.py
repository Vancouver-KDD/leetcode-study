def twoSum(nums, target):
            indexMap = {}

            for i, n in enumerate(nums):
                indexMap[n] = i

            indexMap = dict(sorted(indexMap.items()))
            keyList = list(indexMap.keys())
            print(keyList)


            L, R = 0, len(nums) - 1


            while L < R:
                if keyList[L] + keyList[R] > target:
                        R -= 1
                elif keyList[L] + keyList[R] < target:
                        L += 1
                else:
                    return [indexMap[keyList[L]], indexMap[keyList[R]]]

            # for i in range(len(nums)):
            #     for j in range(i+1, len(nums)):
            #         if target == nums[i] + nums[j]:
            #             return [i, j]


print(twoSum([2, 1, 5, 3], 4))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3,3], 6))
