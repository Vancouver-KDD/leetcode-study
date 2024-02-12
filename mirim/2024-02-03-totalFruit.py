from collections import defaultdict


def totalFruit(fruits: list[int]) -> int:
    size, l, maxCount = 2, 0, 0
    frequencyTree = defaultdict(int)

    for r in range(len(fruits)):
        frequencyTree[fruits[r]] += 1
        if len(frequencyTree) <= size:
            maxCount = max(maxCount, sum(frequencyTree.values()))
        else:
            frequencyTree[fruits[l]] -= 1
            if not frequencyTree[fruits[l]]:
                del frequencyTree[fruits[l]]
            l += 1

    return maxCount


# print(totalFruit([1, 2, 1]), 3)
# print(totalFruit([0, 1, 2, 2]), 3)
# print(totalFruit([1, 2, 3, 2, 2]), 4)
print(totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]), 5)  # 1, 4
