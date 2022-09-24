//limitation: height is null or size is zero, -> return ???? 
// Input: height = [1,8,6,2,5,4,8,3,7] -> Output: 49
// Input: height = [1,1] -> Output: 1
// Time Complexity: O(N) , Space Complexity: O(1)

//
//2022-09-24
class Solution{
    public int maxArea(int[] height){
        
        if(height == null || height.length == 0){
            return 0;
        }
        
        int start = 0;
        int end = height.length - 1;
        int maxAmount = 0; 
        
        while(start < end){
            int curAmount = (end - start) * Math.min(height[start], height[end]);
            maxAmount = Math.max(maxAmount, curAmount);
            
            if(height[start] < height[end]){                
                start++;
            }else{
                end--;
            }
        }
        
        return maxAmount;
    }
}