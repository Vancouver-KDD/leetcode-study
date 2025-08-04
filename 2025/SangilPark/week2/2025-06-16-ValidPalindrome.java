package week2;
import java.util.*;

/*
 * Week 2: Two Pointer & Sliding Window
 * https://leetcode.com/problems/valid-palindrome/
 */
class Solution {
    public static boolean isPalindrome(String s) {
        // two pointer
        s = s.toLowerCase();
        int left = 0, right = s.length() - 1;

        while (left < right) {
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            } else if (!Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            } else {
                if (s.charAt(left) != s.charAt(right)) return false;
                left++;
                right--;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        isPalindrome("A man, a plan, a canal: Panama");
    }
}