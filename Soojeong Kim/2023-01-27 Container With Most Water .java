class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length-1;
        int max = Integer.MIN_VALUE;
        
        while(start<end) {
            max = Math.max(max, (end-start) * Math.min(height[end], height[start]));
            if(height[start] > height[end]) {
                end--;
            }else {
                start++;
            }
        }
        return max;
        //O(logN)
    }
}