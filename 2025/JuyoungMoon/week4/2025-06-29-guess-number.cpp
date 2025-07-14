// Author: Juyoung Moon

// KDD LeetCode Study Week 4: Binary Search.
// https://github.com/juyomo/leetcode-study

// LeetCode #374.
// https://leetcode.com/problems/guess-number-higher-or-lower/

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        return guessHelper(1, n);
    }

    int guessHelper(int low, int high) {
        int mid = low + (high - low) / 2;
        int res = guess(mid);
        if (res == 0) {
            return mid;
        } else if (res == 1) {
            return guessHelper(mid + 1, high);
        } else {
            return guessHelper(low, mid - 1);
        }
    }
};
