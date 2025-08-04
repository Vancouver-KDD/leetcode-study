package week4;
import java.util.*;

/*
 * Week 4: Binary Search
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 */
class Solution {
    public static int search(int[] nums, int target) {
        // binary serach (closed range)
        // kind of sorted array -> guess where the target is
        int left = 0, right = nums.length - 1;      

        while (left <= right) {
            int mid = left + (right - left) / 2;   

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {      // left ascending
                if (nums[left] <= target && target <= nums[mid]) {
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

    public static void main(String[] args) {
        int[] input = {4,5,6,7,0,1,2};
        search(input, 0);
    }
}