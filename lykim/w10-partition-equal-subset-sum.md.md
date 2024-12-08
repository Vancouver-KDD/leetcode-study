## Approach
- Get the sum of the array and set the target, and initialize DP cache arrary to record false/true with the size of target + 1
- Iterate the nums array with a nested loop, index starting from the target to each num
  - DP cache is updated with itself or dp [i - num], which would sum up to the target
- dp[target] will be updated as result

### Complexity
- Time complexity - O(n * target)
- Space complexity - O(target)

### Solution
```
# @param {Integer[]} nums
# @return {Boolean}
def can_partition(nums)
    return false if nums.size == 1
    return false if nums.sum % 2 != 0

    target = nums.sum / 2

    dp = Array.new(target + 1, false)
    dp[0] = true
    for num in nums do
        i = target
        while i >= num do
            dp[i] = (dp[i] || dp[i - num])
            i -= 1
        end
    end

    return dp[target]
end
```
