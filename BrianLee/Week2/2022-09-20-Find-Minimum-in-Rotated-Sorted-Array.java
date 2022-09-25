class Solution {
    public int findMin(int[] nums) {
        if(nums[0] > nums[nums.length-1]) {
            int start = 0;
            int end = nums.length-1;
            while(start < end) {
                int mid = (end-start)/2+start;
                if(mid == 0) mid++;
                if(nums[mid-1] > nums[mid]) return nums[mid];
                else if(mid+1 < nums.length &&
                        nums[mid+1] < nums[mid]) return nums[mid+1];
                else {
                    if(nums[start] > nums[mid-1]) {
                        end = mid-1;
                    } else {
                        start = mid;
                    }
                }
            }
        } else {
            return nums[0];
        }
        return 0;
    }
}