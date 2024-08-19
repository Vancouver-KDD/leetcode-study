/**
 * Leetcode
 * problem: 698
 * link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
 * tag: Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
 */

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = Arrays.stream(nums).sum();
        if (sum % k != 0 || nums.length < k) return false;
        Arrays.sort(nums);

        return canPartitionKSubsets(nums, sum / k, nums.length - 1, new int[k]);
    }

    public boolean canPartitionKSubsets(int a[], int target, int i, int bucket[]) {
        if (i == -1) return true;
        for (int j = 0; j < bucket.length; j++) {
            if (bucket[j] + a[i] <= target) {
                bucket[j] += a[i];
                if (canPartitionKSubsets(a, target, i - 1, bucket)) return true;
                bucket[j] -= a[i];
            }
            if (bucket[j] == 0) break;
        }
        return false;
    }
}