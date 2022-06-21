class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length-1;
        int max =0;
        int area =0;
        while(l<=r) {
            if(height[l] < height[r]) {
                area = height[l]*(r-l);
                if(area>max) max = area;
                l++;
            } else {
                area = height[r]*(r-l);
                if(area>max) max = area;
                r--;
            }
        }
        return max;
    }
}
