/* https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
 * 
 * ## Description 
 * Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be     
 * strictly increasing.
 * 
 * A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for
 * each l <= i < r, nums[i] < nums[i + 1].
 * 
 */

 /**** Sliding Window Solution ****/

 class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int start = 0;
        int result = 0; 
        
        //Iterate while checking if it's increasing or decreasing and moving the pointers depends. 
        for (int end = 0; end < nums.length; end++) {
            
            // if its decreasing, set the start pointer to the current end pointer to move(start over) the window 
            if (end > 0 && nums[end-1] >= nums[end]){
                start = end; 
            }
            
            //Keep updating the result to maximum to find the longest subarray.  
            result = Math.max(result, end - start + 1); 
        }

        return result; 
    }
}

  /**** Two Pointers  Solution ****/

  class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int maxCount = 1;
        int currentCount = 1;
        int i = 0 ;
        int j = 1;

        //Traverse nums array 
        while(j<nums.length)
        {
            //Check if it's increasing 
            if(nums[j]>nums[i])
            {
                //When it is increasing, increase the counter to calculate the length of subarray
                //& Move the pointers to the right to compare further 
                currentCount++;
                i++;
                j++;
            }
            else {
                //When it's not increasing, set the i pointer to j to start over. 
                //move the j to the right, and reset the counter as we are starting over from where it's not increasing. 
                i = j;
                j++;
                currentCount = 1;
            }
            
            //Keep updating the maximum value! 
            maxCount = Math.max(currentCount, maxCount);
        }  
        return maxCount;  
    }
}