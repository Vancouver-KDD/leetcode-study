## Approach_1
- Use Hash structure to record the frequency of each element. Then use the largest k values to get the key
- There's an array method `tally` doing the same job too

### Complexity
- Time complexity - O(nlog(n)) due to sorting
- Space complexity - O(n) with the Hash creation & result array creation of O(k)

### Solution
```
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    hash = Hash.new(0)

    nums.each {|num| hash[num] += 1 }
    frequency = hash.values.sort[-k..-1]

    res = []
    frequency.each do |val|
      key = hash.key(val) 
      res << key
      hash.delete(key)
    end
    
    res
end
```
```
def top_k_frequent(nums, k)
  nums.tally.sort { |(k, v), (k2, v2)| v2 <=> v }.to_h.keys.first(k)
end
```

## Approach_2
- Use bucket sort, array size is bounded to N. 
- Record the 

### Complexity
- Time complexity - O(n) with nested iteration
- Space complexity - O(n) with creating arrays


### Solution
```
```
### Solution
```
```
