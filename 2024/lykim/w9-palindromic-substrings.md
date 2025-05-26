## Approach
- Similar to longest palindromic substrings
- From each index, set the element as a center char of a potential palindrome and expand to the left/right at the same time, incrementing the count when the conditions are met.
- Handle odd/even palindrome cases both

### Complexity
- Time complexity - O(n^2) at worst
- Space complexity - O(1)

### Solution
```
# @param {String} s
# @return {Integer}
def count_substrings(s)
    @res = 0

    for i in 0..(s.size - 1)
        iterate(i, i, s)
        iterate(i, i + 1, s)
    end

    @res
end

private def iterate(l, r, s)
    while l >= 0 && r < s.size && s[l] == s[r]
        @res += 1
        l -= 1
        r += 1
    end 
end
```
