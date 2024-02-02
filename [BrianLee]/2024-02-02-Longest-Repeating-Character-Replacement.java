class Solution {
    public int characterReplacement(String s, int k) {
        int start = 0;
        int end = 0;
        int majority = 0;
        int max = 0;
        int[] letters = new int[26];

        while(end < s.length()) {
            majority = Math.max(majority, ++letters[s.charAt(end)-'A']);

            if(end - start +1 - majority > k)
                letters[s.charAt(start++)-'A']--;

            max = Math.max(max, end - start +1);
            end++;
        }

        return max;
    }
}
