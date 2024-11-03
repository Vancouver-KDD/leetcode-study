## Approach
- backtracking with a recursive depth-first search.
- It allows to select duplicates so we separate the decision tree to handle with duplicates of current or without.
- In each branch, check if the current total is equal to or larger to the target, then break the recursion. Otherwise keep going


### Complexity
- Time complexity - max O(2^n), by the branching factor of the tree in the worst case
- Space complexity - worst O(target*(2^n))

### Solution
```
# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
    @res = []
    @target = target
    @candidates = candidates

    depth_search(0, [], 0)

    @res
end

def depth_search(i, curr, total)
    if total == @target
        @res << curr.dup
        return
    end

    return if i >= @candidates.size || total > @target

    # allowing add duplicates of the current 
    curr << @candidates[i]
    depth_search(i, curr, total + @candidates[i])

    # don't allow add duplicates of the current
    curr.pop()
    depth_search(i + 1, curr, total)
end
```
