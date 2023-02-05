/**
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
 * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
 * Notice that the solution set must not contain duplicate triplets.
 */

// a list of arrays which contains three elements' sum equal to zero

// 1. using sorting and two pointer approach
// time complexity is O(N^2) as we iterate the given array
// in the inner loop, we use two pointers to find the pait that sum = 0
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // create hash set to remove the duplicated list arrays
		Set<List<Integer>> result = new HashSet<>();
		// sort the array
		// to make it easier to check for duplicate values. 
		Arrays.sort(nums);

		// two pointer approach
		// starts at the first index (0) and goes to the second-to-last index
		// we are using nums.length - 2 as the limit
		for (int i = 0; i < nums.length - 2; i++) {
			// start point
			int start = i + 1;
			// end point
			int end = nums.length - 1;
			// we are gonna find the sum of three elements until start pointer passes the end pointer
			// if the sum is equal to 0, the combination will be added to the result list
			while (start < end) {
				int sum = nums[i] + nums[start] + nums[end];
				if (sum == 0) {
					// the next iteration will check the next combination of elements.
					result.add(Arrays.asList(nums[i], nums[start++], nums[end--]));
				}
                if (sum < 0) {
					start++;
				} 
                if(sum > 0) {
					end--;
				}
			}
		}
		return new ArrayList<>(result);
    }
}