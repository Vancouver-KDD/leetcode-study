## Approach
- Similar to the binary search but first check if the right or left portion is sorted or not.
- If the left portion is sorted (by comparing the left and mid point value), check if the target exists there, otherwise set the next iteration to check the right portion.
- Otherwise, check if the target exists in the right side or not, and move the right or left pointer accordingly.

### Complexity
- Time complexity - O(nlog(n))
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    left, right = 0, nums.size - 1
    
    while left <= right do   
        mid = (left + right) / 2
  
        if nums[mid] == target
            return mid
        end

        if nums[left] <= nums[mid] # left side is sorted
            if nums[left] <= target && target <= nums[mid] # confirm target is in the left side
                right = mid
            else
                left = mid + 1
            end
        else # right portion could be partially or fully sorted
            if target >= nums[mid] && target <= nums[right]
                left = mid
            else
                right = mid - 1
            end
        end
    end

    -1
end
```
