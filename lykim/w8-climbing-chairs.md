## Approach
- The first intuition is a brute force way with recursion - depth first search - since this is a decision tree of 1 and 2.
  - But the time complexity is O(2^n) and we can notice there's repetition of the problem
  - To utilize the initially computed problem, use caching - dynamic programming
- With DP approach, if we start from the bottom (end), the solution number is easily determined without going further as it should do when starting from the top.
  - For example, with 10 stairs, for the base cases from the stair #9 to stair #10 there's is only one way. From #10 to #10 is default 1. This is regardless of the number of stairs.
  - From stair #8 to stair #10, 2 ways, based on the two subproblems of from #9-#10, #10-#10, which was already computed.
  - That's why we use the bottom up approach.

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
```
# @param {Integer} n
# @return {Integer}
def climb_stairs(n)
    one, two = 1, 1

    for i in 0..(n - 2)
        temp = one
        one = one + two
        two = temp
    end

    one 
end
```
