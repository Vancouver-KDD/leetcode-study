public class Solution {
    public int MaxProduct(int[] nums) {
        
        int prevMin = nums[0];
        int prevMax = nums[0];
        
        int currMin;
        int currMax;
        
        int globalMax = nums[0];
        int currVal;
        
        
        for(int i = 1; i < nums.Length; i++)
        {
            currVal = nums[i];
            
            currMin = Math.Min(Math.Min(prevMin*currVal, currVal), Math.Min(prevMax*currVal, currVal));
            currMax = Math.Max(Math.Max(prevMin*currVal, currVal), Math.Max(prevMax*currVal, currVal));
            
            globalMax = Math.Max(globalMax, currMax);
            
            prevMin = currMin;
            prevMax = currMax;
            
        }
        
        return globalMax;
        
    }
}