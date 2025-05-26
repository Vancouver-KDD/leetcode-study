## Approach
- First, partitioning in a string is not the same as all combinations.
- backtracking with a recursive depth-first search.
- Start from the first index, then check the whole partition with a loop, if the current string is palindrome (helper function)
- If palindrome, add it to a partition list and keep calling the backtracking recursively. The partition will be added to the result array, once the index goes over the size of the string
- If not palindrome, no need to 


### Complexity
- Time complexity - max O(2^n), by the branching factor of the tree in the worst case
- Space complexity - worst O(target*(2^n))

### Solution
```
# @param {String} s
# @return {String[][]}
def partition(s)
    @res = []
    @partition = []
    @string = s

    backtrack(0)
    @res
end

def backtrack(i)
    if i >= @string.size
        @res << @partition.dup
        return
    end

    for j in i..(@string.size - 1) do
        if is_palindrome(@string, i, j)  # first iteration, it will add single char with recursion. Next iteration will go with the next partition.
            @partition << @string[i..j]
            backtrack(j + 1)
            @partition.pop() # to clean up partition for the next partition.
        end
    end
end

def is_palindrome(s, left, right)
    while left < right
        return false if s[left] != s[right]
        left += 1
        right -= 1
    end

    true
end
```
