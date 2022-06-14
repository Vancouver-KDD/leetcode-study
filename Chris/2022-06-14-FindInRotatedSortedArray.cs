public class Solution {
    public int FindMin(int[] nums) {
        
        int prev = nums[0];
        int curr;
        
        for(int i = 1; i < nums.Length; i++){
            curr = nums[i];
            if(prev > curr){
                return curr;
            }
            prev = curr;
        }
        
        return nums[0];
    }
}