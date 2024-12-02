## Approach
- Utilize house robber 1, only difference is slicing the first or the last element from the array.
- Don't forget to check the case when there's only one num

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    [nums[0], get_max(nums[1..(nums.size-1)]), get_max(nums[0..(nums.size-2)])].max
end

def get_max(nums)
    rob1, rob2 = 0, 0

    for num in nums
        temp = [num + rob1, rob2].max
        rob1 = rob2
        rob2 = temp   
    end
        
    rob2
end
```
