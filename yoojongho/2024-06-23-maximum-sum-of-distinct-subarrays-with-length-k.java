/**
 * Leetcode
 * problem: 2461
 * link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
 */

/**
 * Approach
 * 1. To optimize runtime, update the sum value by adjusting it with the values at the left and right pointers.
 * 2. To avoid calculating repeated values, store values in the 'storage' and verify that the next value is not a duplicate.
 */
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        long result = 0;
        long sum = 0;
        int r = 0;
        Set<Integer> storage = new HashSet<>();
        for (int l = 0; l < nums.length; l++) {
            while (r < nums.length && storage.size() < k && !storage.contains(nums[r])) {
                storage.add(nums[r]);
                // #1
                sum += nums[r];
                r++;
            }
            if (storage.size() == k && result < sum) {
                result = sum;
            }
            storage.remove(nums[l]);
            // #1
            sum -= nums[l];
        }
        return result;
    }
}