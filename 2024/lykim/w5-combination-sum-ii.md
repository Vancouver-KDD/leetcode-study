## Approach
- backtracking with a recursive depth-first search.
- It doesn't allows to select duplicates, so the decision tree is branching by including the next value or not.
- In each branch, check if the current total is equal to or larger to the target, then break the recursion. Otherwise keep going

### Complexity
- Time complexity - max O(2^n), by the branching factor of the tree in the worst case
- Space complexity - worst O(target*(2^n))

### Solution
```
# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum2(candidates, target)
    @res = []
    @candidates = candidates.sort

    backtrack(0, [], target)

    @res
end

def backtrack(start_position, curr, target)
    if target == 0
        @res << curr.dup
    end

    return if target <= 0

    prev = -1
    for i in start_position..(@candidates.size - 1) do
        next if @candidates[i] == prev  # checking if this candidates is already selected, then skip
        
        curr << @candidates[i]
        backtrack(i + 1, curr, target - @candidates[i])
        curr.pop() #to avoid duplicates

        prev = @candidates[i]
    end
end
```
