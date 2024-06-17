public class Solution {
    public int MaxArea(int[] height) {
        int l = 0;
        int r = height.Length-1;
        int max =0;
        while(l<r){
            int c_height = Math.Min(height[l],height[r]);
            max = Math.Max(max, c_height * (r-l));

            if(height[l]>=height[r]){
                r--;
            }else{
                l++;
            }
        }
        return max;
    }
}
// TC: O(n);
// SC: O(1);
