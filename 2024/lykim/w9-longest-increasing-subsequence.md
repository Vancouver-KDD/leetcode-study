## Approach
- Initialize an array to cache with the length of the nums array, and with value of 1 for all as a base case)
- Iterate from the last, and at each iteration, loop from the last to the index, record if the sequence is increasing
  - Then in the outer loop, record the max each time then lastly return it

### Complexity
- Time complexity - O(n^2) 
- Space complexity - O(n)

### Solution
```
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)

    dp = Array.new(nums.size, 1)
    dp[nums.size - 1] = 1

    i = nums.size - 2
    max = 1
    while i >= 0 do
        j = nums.size - 1
        temp = 1
        
        while j >= i do
            if nums[i] < nums[j]
                temp = [dp[j] + 1, temp].max
            end
            j -= 1
        end
        
        dp[i] = temp
        max = [dp[i], max].max
        i -= 1
    end
    
    max
end
```
