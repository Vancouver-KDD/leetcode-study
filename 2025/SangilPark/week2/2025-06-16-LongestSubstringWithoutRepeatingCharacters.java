package week2;
import java.util.*;

/*
 * Week 2: Two Pointer & Sliding Window
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
class Solution {
    public static int lengthOfLongestSubstring(String s) {
        // sliding window
        // repeating X -> count char in window
        // adjust the window size
        // 1. iterate over String s -> expand window size
        // 2. if repeating char -> shrink window size
        // 3. update longest size
        // tc : "abcabcabc", "a1a", "a&a"
        Set<Character> count = new HashSet<>();
        int longest = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            while (count.contains(c)) {
                count.remove(s.charAt(left));
                left++;
            }
            count.add(c);
            longest = Math.max(right - left + 1, longest);
        }
        
        return longest;
    }

    public static void main(String[] args) {
        lengthOfLongestSubstring("abcabcbb");
    }
}