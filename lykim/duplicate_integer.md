### Approach
- Use a data structure that doesn't contain duplicates, Hash set.
- Iterate the given array and construct a set, add? method will tell me if the element is already in the set or not

### Complexity
- Time complexity - O(n) with the array iteration
- Space complexity - O(n) with the Set creation

### Solution
```
# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    return false unless nums.size > 1
    
    set = Set.new
    
    nums.each do |num|
        return true unless set.add?(num)
    end

    false
end
```
