public class Solution {
    public int FindMin(int[] nums) {
        // values
        int prev = nums[0];
        int curr;
        
        // indices
        int low = 0;
        int high = nums.Length -1;
        int mid;
        
        // in case of not rotated array.
        // = is for an array of size one.
        if(nums[low] <= nums[high]){
            return nums[0];
        }
        
        while(true){
            //set current
            mid = (low + high) / 2;
            curr = nums[mid];

            //check if the next value is the beginning of the original array
            if(curr > nums[mid+1]){
                return nums[mid+1];
            }
            
            //update index (binary search)
            if(curr > prev){
                low = mid;
            } else {
                high = mid;
            }
            
            prev = curr;
        }
        
    }
}