class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int max = 0;

        int start = 0;
        for(int end = 0; end < s.length(); end++) {
            count[s.charAt(end)-'A']++;

            while(((end - start + 1) - getMajority(count)) > k) {
                count[s.charAt(start++)-'A']--;
            }

            max = Math.max(max, end - start + 1);
        }

        return max;
    }

    private int getMajority(int[] count) {
        int max = 0;
        for(int i = 0; i < 26; i++) {
            max = Math.max(max, count[i]);
        }
        return max;
    }
}
