## Approach_1
- Use [ruby group_by method](https://www.rubydoc.info/stdlib/core/Enumerable:group_by) with sorting each element - library method

### Complexity
- Time complexity - O(nlog(n)) with sorting, and group_by doesn't add?
- Space complexity - O(n) with the Hash creation by group_by

### Solution
```
# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    strs.group_by { |str| str.chars.sort }.values
end
```

## Approach_2
- Without using library methods
- Initialize a hash for the result and also initialize an array of length 26 and record the ascii number of each char of the element. Anagrams would have the same array, so it becomes key of the result hash and each element is added as a value of the key.
- Return the values of the hash for the answer

### Complexity
- Time complexity - O(n^2) with nested iteration
- Space complexity - O(n) with creating arrays for each element + result hash O(1)

### Solution
```
def group_anagrams(strs)
    res = Hash.new

    strs.each_with_index do |str, i|
        ans = Array.new(26, 0)
        str.chars.each do |char|
            ans[char.ord - "a".ord] += 1 # record the alphabet order as ascii number. a => 0, b=> 1.... Record all occurrences of each alphabet
        end

        res[ans] ||= []
        res[ans].push(str)
    end

    res.values
end
```
