package week2;
import java.util.*;

/*
 * Week 2: Two Pointer & Sliding Window
 * https://leetcode.com/problems/longest-repeating-character-replacement/
 */
class Solution {
    public static int characterReplacement(String s, int k) {
        // sliding window
        // maxCnt를 줄이지 않아도 `>k` 조건으로 윈도우 사이즈를 앞쪽에서 줄이기 때문에 문제없단다
        int[] cnt = new int[26];        // [A=2, B=2]
        
        int longest = 0;
        int maxCnt = 0;     
        int left = 0;       // 3

        for (int right = 0; right < s.length(); right++) {      // 6
            cnt[s.charAt(right) - 'A']++;
            maxCnt = Math.max(cnt[s.charAt(right) - 'A'], maxCnt);      // 3

            int windowSize = right - left + 1;      // 5
            if (windowSize - maxCnt > k) {
                cnt[s.charAt(left) - 'A']--;
                left++;
            } else {
                longest = Math.max(windowSize, longest);    // 4
            }
        }
        return longest;
    }

    public static void main(String[] args) {
        characterReplacement("ABAB", 2);
    }
}