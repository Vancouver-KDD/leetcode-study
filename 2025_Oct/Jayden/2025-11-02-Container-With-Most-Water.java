class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public int maxArea(int[] height) {
        int right = height.length - 1;
        int left = 0;
        int maxArea = 0;

        // loop untill left and right pointers meet each other
        while (left < right) {
            int currentHeight = Math.min(height[left], height[right]);
            int currentWidth = right - left;
            int currentArea = currentWidth * currentHeight;

            // update the pointer that has shorter height
            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }

            maxArea = Math.max(maxArea, currentArea);
        }

        return maxArea;
    }
}