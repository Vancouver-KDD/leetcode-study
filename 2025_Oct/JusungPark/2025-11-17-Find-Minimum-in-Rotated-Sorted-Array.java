public int findMin(int[] nums) {
    int left = 0, right = nums.length - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;


        // if mid is greater than right, the minimum value is on the right
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else { 
            // if mid is less than right, the minimum value is on the left
            right = mid;
        }
    }

    return nums[left]; // left == right is the minimum value's position
}
