import collections


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            count[fruit] = count.get(fruit, 0) + 1
            total += 1

            while len(count) > 2:
                left_fruit = fruits[l]
                count[left_fruit] -= 1
                total -= 1
                l += 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
            res = max(res, total)

        return res


# [0, 1, 2, 2]
# l
# r
# Count: {0: 1}

# [0, 1, 2, 2]
#  l
#      r
# Count: {0: 1, 1: 1}

# [0, 1, 2, 2]
#     l
#         r
# Count: {1: 2, 2:1}

# [0, 1, 2, 2]
#     l
#            r
# Count: {1: 2, 2:2}


# 1. for loop iterates through trees (fruits) from left to right.
# 2. count keeps track of fruit counts in the current window.
# 3. while loop shrinks the window to contain at most two distinct fruit types.
# 4. It moves the left pointer (l) and updates count and total accordingly.
# 5. res stores the maximum window size, representing the max fruits collected.
# 6. The code returns res
