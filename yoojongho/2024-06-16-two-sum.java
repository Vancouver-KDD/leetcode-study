/**
 * Leetcode
 * problem: 1
 * link: https://leetcode.com/problems/two-sum/description/
 * tag: Two Pointers
 */

/**
 * Approach
 * 1. Iterate the array twice.
 * 2. Check pairs of elements except same element or already checked elements.
 * 3. If the sum of value equals the target, return the current indices as an array
 * 4. If no such a pair is found, return an empty array.
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // #1
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                // #2
                if (nums[i] + nums[j] == target) {
                    // #3
                    return new int[]{i, j};
                }
            }
        }
        // #4
        return new int[]{};
    }
}