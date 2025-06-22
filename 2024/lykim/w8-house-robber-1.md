## Approach
- Keep two values (prev, prev -1) to record max amount that can be robbed at each index, and use the previously computed value to compute the current max

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
Better runtime one
```
# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    rob1, rob2 = 0, 0

    for num in nums
        temp = [num + rob1, rob2].max
        rob1 = rob2
        rob2 = temp   
    end
        
    rob2
end
```


```
# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    return nums[0] if nums.size == 1

    max = [nums[0], [nums[0], nums[1]].max]
    i = 2
    while i < nums.size do
        max[i] = [max[i - 2] + nums[i], max[i - 1]].max if i <= 2
        max[i] = [max[i - 3] + nums[i], max[i - 2] + nums[i], max[i - 1]].max if i > 2
        i += 1
    end

    max.max()
end
```

