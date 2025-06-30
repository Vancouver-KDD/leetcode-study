package week4;
import java.util.*;

/*
 * Week 4: Binary Search
 * https://leetcode.com/problems/binary-search/
 */
class Solution {
    public static int search(int[] nums, int target) {
        int left = 0, right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] input = {-1,0,3,5,9,12};
        search(input, 9);
    }
}