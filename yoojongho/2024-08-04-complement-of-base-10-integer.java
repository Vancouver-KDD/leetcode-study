/**
 * Leetcode
 * problem: 1009
 * link: https://leetcode.com/problems/complement-of-base-10-integer/description/
 * tag: Bit Manipulation
 */

class Solution {
    public int bitwiseComplement(int n) {
        if(n == 0) return 1;
        int result = 0;
        int counter = 0;
        while (n > 0){
            int digit = n % 2;
            if(digit == 1) digit = 0;
            else digit = 1;
            result += digit * Math.pow(2, counter);
            n /= 2;
            counter++;
        }
        return result;
    }
}