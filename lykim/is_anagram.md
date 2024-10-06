### Approach
- Use a data structure to record the occurrences by key, Hash map.
- Iterate the given arrays, increase first then decrease for the second one.
- Then check if the result hash value only should contain one 0.

### Complexity
- Time complexity - O(n) with the array iterations
- Space complexity - O(n) with the Hash creation

### Solution
```
def is_anagram(s, t)
    return false if s.length != t.length

    hash = Hash.new(0)
    
    s.each_char do |char|
        hash[char] += 1
    end

    t.each_char do |char|
        if hash.key?(char)
            hash[char] -= 1
        else
            return false
        end
    end

    hash.values.uniq == [0]
end
```
