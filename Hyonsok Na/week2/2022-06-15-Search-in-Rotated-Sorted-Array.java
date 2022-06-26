class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length < 1) {
            return -1;
        }
        
        int mid, left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            mid = left + ((right - left) / 2);
            
            // if found, return mid -- index!!
            if (nums[mid] == target) return mid;
            
            // one side will alwasy be sorted
            if (nums[mid] >= nums[left]) {
                // is target on left?
                if (target >= nums[left] && target <= nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // is target on right?
                if (target <= nums[right] && target >= nums[mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        // not found
        return -1;
    }
}

