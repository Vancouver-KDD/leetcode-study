// limitation : if nums is null or size is zero return what?????
// Input: nums = [2,3,-2,4]  -> Output: 6
// Input: nums = [-2,0,-1] -> Output: 0
// Input: [-2,3,-4] -> Output: 24

//Time Complexity: O(n),  Space Complexity: O(1)
//
class Solution{
    
    public int maxProduct(int[] nums){
        
        if(nums == null || nums.length == 0){
            return 0; 
        }
        
        int max = nums[0]; 
        int curContigMin = nums[0];
        int curContigMax = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            
            int upDatedContigMin = curContigMin * nums[i];
            int upDatedContigMax = curContigMax * nums[i];
            
            //find current contiguous mininum product
            curContigMin = Math.min(upDatedContigMin, Math.min(upDatedContigMax , nums[i]));
            //find current contiguous maximum product
            curContigMax = Math.max(upDatedContigMin, Math.max(upDatedContigMax , nums[i]));
            //maximum product so far
            max = Math.max(curContigMax, max);
        }
        
        return max;
        
    }
}
