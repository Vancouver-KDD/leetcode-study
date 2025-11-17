class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // if mid is greater than right, it means there is no val that's less than mid on the left side
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[right];
    }
}