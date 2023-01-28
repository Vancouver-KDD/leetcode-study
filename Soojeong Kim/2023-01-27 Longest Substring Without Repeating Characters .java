import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0, max = 0;
        Set<Character> set= new HashSet<>();
        int len = s.length();

        while(j<len) {
            if(!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                max = Math.max(max, set.size());
            }else {
                set.remove(s.charAt(i++));
            }
        }
        return max;
    }
}
