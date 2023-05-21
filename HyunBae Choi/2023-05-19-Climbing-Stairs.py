# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Constraints:
# 1 <= n <= 45

# 1. define the base case:
#    if the number of steps go past n, return 0
# 2. we can use dynamic programming to solve the problem:
#    if we look at the problem with a decision tree using bottom-up DFS,
#    we can find out that the solution at the current step depends on the sum of all possible solutions in the previous 2 steps
#    therefore, set first and second to equal to 1 solution initially
# 3. save first into temp, assign new first as first + second (sum of all possible solutions for the last 2 steps), assign second as first (temp)
# 4. repeat until n - 1
# 5. return first


class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1

        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp

        return first