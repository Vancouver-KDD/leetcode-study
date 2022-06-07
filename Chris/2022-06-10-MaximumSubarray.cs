public class Solution {
    public int MaxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];
        
        for(int i = 1; i < nums.Length ; i++){
            
            if(currentSum < 0){
                currentSum = nums[i];
            } else {
                currentSum += nums[i];    
            }
            
            if(currentSum > maxSum){
                    maxSum = currentSum;
                }
             
        }
        
        return maxSum;
    }
}