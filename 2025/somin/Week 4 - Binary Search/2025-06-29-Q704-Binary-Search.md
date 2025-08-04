## 704. Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

### Solution

```
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        
        while(left<=right){
         int mid = left + ( right - left ) /2;
            if(nums[mid] == target){
                return mid;
            }else if (nums[mid] < target){
                left = mid+1;
            }else if (nums[mid] > target){
                right = mid-1;
            }
            
        }
        return -1;
        
    }
}
```

## Time Complexity: O(log n)
Because in each iteration, the search range is reduced by half. This divide-and-conquer approach results in a logarithmic number of steps relative to the input size.

## Space Complexity: O(1)
Only a constant number of variables (left, right, mid) are used regardless of the input size. No extra data structures or recursion are used, so the memory usage stays constant.
