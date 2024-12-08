## Approach
- Keep the max (global) and the max product at the current index, and also min product at the current index - this is due to multiplying the two negative values case, to keep the max absolute value. 
- Iterate the nums array and set the max with the [max, current max] by multiplying the current value with the max
- Don't forget to set temp current max, when setting the current min. Since the current max is already changed 

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    max_product = nums[0]
    current_max = 1
    current_min = 1

    nums.each do |number|
        temp_current_max = current_max * number
        current_max = [number, temp_current_max, current_min * number].max
        current_min = [number, temp_current_max, current_min * number].min
        max_product = [current_max, max_product].max
    end

    max_product
end
```
