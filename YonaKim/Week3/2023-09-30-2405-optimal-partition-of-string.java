import java.util.Arrays;

class Solution {
    public int partitionString(String s) {
        int[] helper = new int[26];
        Arrays.fill(helper, -1);
        int minResult = 1;
        int startSubstring = 0;

        for(int i = 0; i < s.length(); i++) {
            if(helper[s.charAt(i) - 'a'] >= startSubstring) {
                minResult++;
                startSubstring = i;
            }
            helper[s.charAt(i) - 'a'] = i;
        }
        
        return minResult;
    }
}