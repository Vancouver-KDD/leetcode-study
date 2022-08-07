class Solution {
    public int characterReplacement(String s, int k) {
        int[] a = new int[26];
        int max = 0, i = 0, j = 0;
        a[s.charAt(0) - 'A']++;
        while (j != s.length()) {
            if (i > j) {
                j++; continue;
            }
            int thisMax = 0;
            for (int m = 0; m < a.length; m++) {
                thisMax = Math.max(thisMax, a[m]);
            }
            if (j - i + 1 - thisMax <= k) {
                max = Math.max(j - i + 1, max);
            }
            else {
                a[s.charAt(i) - 'A']--;
                i++;
            }
            j++;
            if (j != s.length()) a[s.charAt(j) - 'A']++;
        }
        return max;
    }
}