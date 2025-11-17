class Solution {
    /**
        Time Complexity: O(log(n))
        Space Complexity: O(n)
     */
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {

                // check if the target exists between the range
                if (nums[left] <= target && nums[mid] > target) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            } else {

                // check if the target exists between the range
                if (nums[right] >= target && nums[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
        }

        if (nums[left] == target) return left;

        return -1;
    }
}