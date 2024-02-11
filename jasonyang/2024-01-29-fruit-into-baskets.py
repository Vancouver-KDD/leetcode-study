# LeetCode 904. Fruit Into Baskets 
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
#
# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a single type of fruit.
# There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
# The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
#
# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to store the count of each type of fruit in the current window
        count = {}
        max_fruits = 0
        start = 0

        for end in range(len(fruits)):
            # Add the current fruit to the window
            if fruits[end] not in count:
                count[fruits[end]] = 0
            count[fruits[end]] += 1

            # If more than two types of fruits are in the window, move the start
            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1

            # Update the maximum number of fruits
            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits

# Example usage
sol = Solution()
print(sol.totalFruit([1, 2, 1]))  # Output: 3
print(sol.totalFruit([0, 1, 2, 2]))  # Output: 3
print(sol.totalFruit([1, 2, 3, 2, 2]))  # Output: 4