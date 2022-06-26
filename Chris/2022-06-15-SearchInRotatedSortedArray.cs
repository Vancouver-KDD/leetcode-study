public class Solution {
    public int Search(int[] nums, int target) {
        
        int low = 0;
        int high = nums.Length-1;
        int mid = (low + high) / 2;
        
        int lowVal;
        int highVal;
        int midVal;
        
        while(low <= high){
            
            lowVal = nums[low];
            highVal = nums[high];
            midVal = nums[mid];

            
            
            if(midVal == target){
                return mid;
            }
            
            if(lowVal < highVal){
                if(target > midVal){
                    low = mid+1;
                } else {
                    high = mid-1;
                }
            } else if(midVal < highVal){
                if(target >= lowVal || target < midVal){
                    high = mid-1;
                } else {
                    low = mid+1;
                }
            } else {
                if(target <= highVal || target > midVal){
                    low = mid+1;
                } else{
                    high = mid-1;
                }
            }
            mid = (low + high) / 2;
            
        }
        return -1;
        
        
        
    }
}