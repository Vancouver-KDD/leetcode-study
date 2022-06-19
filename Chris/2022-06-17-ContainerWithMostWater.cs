public class Solution {
    public int MaxArea(int[] height) {
        
        int r = height.Length - 1;
        int l = 0;
        int maxArea = 0;
        
        
        while(r > l){
            maxArea = Math.Max(maxArea, Math.Min(height[l],height[r])*(r-l));
            if(height[r] > height[l]){
                l++;
            } else {
                r--;
            }
        }
        
        return maxArea;
        
        
    }
}