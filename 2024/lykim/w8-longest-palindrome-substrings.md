## Approach
- From each index, set the element as a center char of a potential palindrome and expand to the max palindrome, keeping the longest palindrome as res.
- Handle odd/even palindrome cases both

### Complexity
- Time complexity - O(n^2)
- Space complexity - O(1)

### Solution
```
# @param {String} s
# @return {String}
def longest_palindrome(s)
    @res = ""
    @size = 0

    for i in 0..(s.size - 1)
        iterate(i, i, s)
        iterate(i, i + 1, s)
    end

    @res
end

private def iterate(l, r, s)
    while l >= 0 && r < s.size && s[l] == s[r]
        if (r - l + 1) > @size
           @res = s[l..r]
           @size = r - l + 1
        end
        l -= 1
        r += 1
    end 
end
```
