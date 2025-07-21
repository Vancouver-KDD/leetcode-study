import copy


def subsets(nums):
    result = [[]]

    for num in nums:
        subs = copy.deepcopy(result)

        for sub in subs:
            sub.append(num)

        result += subs

    return result


print(subsets([1, 2, 3]))
