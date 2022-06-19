// couldn't solve
class Solution {
    public int search(int[] nums, int target) {
        if(nums.length != 0) {
        if(target < nums[0]) {
            for(int i = nums.length/2+1; i<nums.length; i++) {
                if(nums[i] == target) {
                    return i;
                } else {
                    return -1;
                }
            }
        } else {
            for(int i = 0; i<=nums.length/2; i++) {
                if(nums[i] == target) {
                    return i;
                } else {
                    return -1;
                }
            }
        }
        }
        return -1;
        
    }
}

//from reference
class Solution {
    // in rotated sorted array atleast one half will be sorted.
    // Apply binary search in that half
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        
        while (l <= r) {
            int mid = l + (r-l)/2;
        
            if (nums[mid] == target) {
                return mid;
            } else if (nums[l] <= nums[mid]) {
                // means first half is sorted
                if (target >= nums[l] && target < nums[mid]) {
                    r = mid-1;
                } else {
                    l = mid+1;
                }
            } else {
                // means 2nd half is sorted
                if (target > nums[mid] && target <= nums[r]) {
                    l = mid+1;
                } else {
                    r = mid-1;
                }
            }
        }
        return -1;
    }
}