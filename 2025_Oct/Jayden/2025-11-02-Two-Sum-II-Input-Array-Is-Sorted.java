class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public int[] twoSum(int[] numbers, int target) {
        int right = numbers.length - 1;
        int left = 0;

        // loop untill both pointers meet each other
        while (left < right) {
            int sum = numbers[left] + numbers[right];

            /**
             * if the current sum equals the target, found the pair.
             *
             * if the current sum is greater than the target, it means the right pointer is too large, decrement it to reduce the sum.
             *
             * If the current sum is less than the target, the left pointer is too small, increment it to increase the sum.
             */
            if (sum == target) {
                return new int[] { left + 1, right + 1 };
            } else if (sum > target) {
                right--;
            } else {
                left++;
            }
        }

        return new int[2];
    }
}