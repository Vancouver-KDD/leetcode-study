class Solution {
    public int search(int[] nums, int target) {
        // [3,4,5,6,1,2]
        // 
        //1) left < mid  left side ordered
        // if left < target < mid
        //  -> right = m - 1
        // else remove left side -> left = m + 1
        //2) mid < right right side ordered 
        // if m < target< right
        //   left = m + 1
        // else remove the right side  right = m - 1

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {

            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid] ) { // 주의 when left == mid

                if (nums[left] <= target && target < nums[mid]) {

                    right = mid - 1;

                } else {
                    left = mid + 1;
                }

            } else {

                if (nums[mid] < target && target <= nums[right]) {

                    left = mid + 1;

                } else {
                    right = mid - 1;
                }

            }


        }

        return -1;

    }
}