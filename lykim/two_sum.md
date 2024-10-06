### Approach
- Store the difference to the target for each element of the array, and index.
- To facilitate look-up with key, use Hash to record
- Iterating the array, if the current number is already in the hash map, return the indices, or store the difference.

### Complexity
- Time complexity - O(n) with the array iteration
- Space complexity - O(n) with the Hash creation

### Solution
```
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = Hash.new

    nums.each_with_index do |num, i|
        difference = target - num
        
        if hash.key?(num)
            return [hash[num], i]
        else
            hash[difference] = i
        end
    end
end
```
