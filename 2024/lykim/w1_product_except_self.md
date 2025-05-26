## Approach_1
- In the result array, store the prefix product with the first iteration, then iterate from the last again with a suffix product

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    res = Array.new(nums.size, 1)

    prefix, postfix = 1, 1
    nums.each_with_index do |num, i|
        res[i] = prefix
        prefix *= nums[i]
    end

    for i in (1..nums.size) do
        res[-i] *= postfix
        postfix *= nums[-i]
    end

    res
end
```
