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
- Use bucket sort - create a frequency record array with size bounded to N, each element indicating the occurrence of num

### Complexity
- Time complexity - O(n)
- Space complexity - O(n) with creating the tally hash and frequency array


### Solution
```
def top_k_frequent(nums, k)
    count_hash = nums.tally
    frequency = Array.new(nums.size)

    count_hash.each do |key, val|
        if frequency[val]
            frequency[val] << key
        else
            frequency[val] = [key]
        end
    end


    frequency.flatten.compact.last(k) # with flatten & compact, clean up the array and fetch the last k keys only
end
```
