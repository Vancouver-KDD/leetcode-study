## Approach
- Start from the midpoint and compare with the target. Run the function recursively

### Complexity
- Time complexity - O(log(n))
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    binary(0, nums.length - 1, nums, target)          
end

def binary(left, right, nums, target)
    return -1 if left > right
    mid = (left + right) / 2

    if target == nums[mid]
        return mid
    elsif target > nums[mid]
        return binary(mid + 1, right, nums, target)
    else
        return binary(left, mid - 1, nums, target)
    end

    return -1
end
```
