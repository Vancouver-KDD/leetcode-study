## Approach
- Contemplate about the condition to determine at which side the mininum exists - draw the permutations
- if mid point is larger than the very right value, the minimum is at the right side. Otherwise, at the left side.

### Complexity
- Time complexity - O(logn)
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    binary_search_min(0, nums.length - 1, nums)
    
    # real code with library
    # nums.bsearch { |num| num <= nums.last } 
end

def binary_search_min(left, right, nums)
    return nums[left] if left == right
    mid = (left + right) / 2

    if nums[mid - 1] > nums[mid]  # mid - 1 will return the last value if mid - 1 < 0, so still valid condition
        return nums[mid]
    end

    if nums[mid] > nums[right] # min exists in the right side 
        binary_search_min(mid + 1, right, nums)
    else
        binary_search_min(left, mid - 1, nums)
    end
end
```
