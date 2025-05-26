## Approach
- With two pointers, move right until all chars in the windows cover the `t`. Once it's covered move left until it's still covered.
- To check if `t` chars are included in the current window, keep a hash counting the occurrences. 

### Complexity
- Time complexity - O(n)
- Space complexity - O(k)

### Solution
```
# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    res = ""
    return res if s.size < t.size

    left, right = 0, 0

    hash = Hash.new(0)
    t.chars.each { |char| hash[t] += 1 }
    copy_hash = hash.dup

    while right - left + 1 > t.size do
        hash[s[right]] -= 1

        unless hash.values.any? { |value| value > 0 }
            if s[left..right].size < res.size || res.empty?
              res = s[left..right]
            end
     
            left += 1
            hash = copy_hash
        end

        right += 1
    end

    res
end
