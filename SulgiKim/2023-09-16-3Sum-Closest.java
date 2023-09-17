/*
 * ## Description

    Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.
    Return the sum of the three integers.
 * 
 *  Iterate all the possible combination and compare to find the closest sum to 'target'
 *  For optimization: Two pointers with a fixed pointer i
 */

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);

        int n = nums.length;
        int closestSum = nums[0] + nums[1] + nums[2]; 
				
        // i as a fixed pointer while moving the left, right pointers 
        // Only iterating until n - 2 because the combination of three numbers is needed. 
        for (int i = 0; i < n - 2; i++) {

            // Define pointers left and right to get closestSum
            int left = i + 1; //Next number of i 
            int right = n -1; //Number at the end of the array 
						
            // Traverse through remaining elements of list for each i value
            while(left < right) {
                // Define currentSum which will be used to compare with closestSum
                int currentSum = nums[i] + nums[left] + nums[right]; 
                
                //Compare the differences between target with currentSum and with closestSum 
                //If the difference between target and currentSum is smaller than the one with closestSum, assign currentSum value into closestSum.
                if(Math.abs(target - currentSum) < Math.abs(target - closestSum)){
                    closestSum = currentSum; 
                }

                if(currentSum < target) {
                    left++; // If current sum is less than we need, move the left pointer to the right 
                } else {
                    right--; // If current sum is higher than we need, move the right pointer to the left 
                }
            }
        }

        return closestSum;
    }
}