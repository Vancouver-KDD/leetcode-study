package week4;
import java.util.*;

/*
 * Week 4: Binary Search
 * https://leetcode.com/problems/guess-number-higher-or-lower/
 */
class Solution {
    public static int guessNumber(int n) {
        int left = 1, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int result = guess(mid);        // pre-defined API

            if (result == 0) {
                return mid;
            } else if (result < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] input = {-1,0,3,5,9,12};
        guessNumber(10);
    }
}