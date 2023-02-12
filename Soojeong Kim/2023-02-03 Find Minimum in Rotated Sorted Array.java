class Solution {
    public int findMin(int[] nums) {
        //ascending order 
        //rotate -> not ascending order
        //O(logN) -> can't check in order
        //binary search
        //return minimum of the array
        int start = 0;
        int end = nums.length-1;

        while(start<end) { 
            int mid = start + (end-start)/2;
            if(nums[mid]<nums[end]) {
                end = mid;
            }else {
                start = mid +1;
            }
        }
        return nums[start];
    }
}