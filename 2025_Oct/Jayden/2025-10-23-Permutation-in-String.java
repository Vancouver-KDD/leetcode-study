class Solution {
    /**
        let n = length of s2

        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public boolean checkInclusion(String s1, String s2) {

        if (s1.length() > s2.length()) return false;

        // index represents the position of each lowercase English letter [a-z]
        // frequency of characters will be stored at each index
        int[] s1Freq = new int[26];
        int[] s2Freq = new int[26];
        int windowSize = s1.length();

        // initialize the first window
        for (int i = 0; i < windowSize; i++) {
            s1Freq[s1.charAt(i) - 'a'] += 1;
            s2Freq[s2.charAt(i) - 'a'] += 1;
        }

        if (Arrays.equals(s1Freq, s2Freq))
            return true;

        // slide window and update frequency array during iteration
        for (int i = windowSize; i < s2.length(); i++) {
            s2Freq[s2.charAt(i - windowSize) - 'a'] -= 1;
            s2Freq[s2.charAt(i) - 'a'] += 1;

            if (Arrays.equals(s1Freq, s2Freq))
                return true;
        }

        return false;
    }
}