/*
* ## Description

    Given an integer array `nums` sorted in non-decreasing order, return *an array of the squares of each number sorted in non-decreasing order.

 *  As the array nums is sorted in non-decreasing order, it implies that the biggest squared number is placed in either left or right end of  array. 
 *  Therefore, the biggest number will be stored first at the end of result array while comparing the left and right ends of nums array. 
 */

class Solution {
    public int[] sortedSquares(int[] nums) {
        //Initialize the left and right pointer to the both ends of array 
        int left = 0;
        int right = nums.length - 1; 

        //Assign the result array to return as the same size as the nums array. 
        int[] result = new int[nums.length];
        
        //i as a last index of the result array to store the biggest squared value from nums array
        int i = nums.length - 1; 

        //Traverse until left pointer and right pointer meet 
        while (left <= right){ 

            //Compare absolute value so we can assess which one will be bigger when squared 
            if(Math.abs(nums[left]) < Math.abs(nums[right])){
                result[i] = nums[right] * nums[right];
                right--; //Move right pointer to the left as we stored the squared value of right already. 
            } else {
                result[i] = nums[left] * nums[left];
                left++; //Move left pointer to the right as we stored the squared value of left already. 
            }
            i--; 
        }

        return result;

    }
}