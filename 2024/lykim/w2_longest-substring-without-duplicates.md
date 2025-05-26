## Approach
- Keep two pointers indicating the first and the last index of the substring
- keep the longest length as result
- Keep moving last pointer to the right and add the element to the Set, until the new element is found duplicate
- If duplicate found, clear up the hash move the first pointer to the right

### Complexity
- Time complexity - O(n)
- Space complexity - O(n)

### Solution
```
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
   first, last = 0, 0
   res = 0

   set = Set.new

   while last < s.length do
      until set.add?(s[last])
        set.delete(s[first])
        first += 1
      end
    
      res = [res, set.size].max
      last += 1
   end

   res
end
```
