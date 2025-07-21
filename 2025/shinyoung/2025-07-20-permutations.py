import copy


def subsets(nums):
    result = []

    per = []

    def dfs():
        if len(per) == len(nums):
            result.append(per[:])
            return

        for num in nums:
            if num not in per:
                per.append(num)
                dfs()
                per.pop()

    dfs()

    return result


print(subsets([1, 2, 3]))
