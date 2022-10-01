class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        while(start <= end) {
            int mid = (end-start)/2+start;
            if(nums[mid] == target) return mid;
            if(mid-1 >= 0 && nums[mid-1] == target) return mid-1;
            if(mid+1 < nums.length && nums[mid+1] == target) return mid+1;
            else {
                if(mid-1 >= 0 && nums[start] <= nums[mid-1]) {
                    if(nums[start] <= target && target <= nums[mid-1]) {
                        end = mid-1;
                    } else {
                        start = mid+1;
                    }
                } else {
                    if(nums[mid] < target && target <= nums[end]) {
                        start = mid+1;
                    } else {
                        end = mid-1;
                    }
                }
            }
        }
        return -1;
    }
}