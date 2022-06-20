class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        if(nums.length==1) return nums[0];
        if(nums[0]<nums[r]) return nums[0];
        while(l<=r) {
            int mid = l+(r-l)/2;
            if(nums[mid]>nums[mid+1]) {
                return nums[mid+1];
            }
            if(nums[mid]<nums[mid-1]) {
                return nums[mid];
            }
            if(nums[mid]>nums[0]) {
                l=mid+1;
            } else {
                r=mid-1;
            }
        }
        return -1;
    }
}