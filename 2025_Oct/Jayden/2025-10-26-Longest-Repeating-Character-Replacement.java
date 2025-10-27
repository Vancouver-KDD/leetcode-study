class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public int characterReplacement(String s, int k) {

        // stores the frequency of each uppercase characters [A-Z] in current window
        int[] freq = new int[26];

        int windowSize = 0;
        int maxFreq = 0;
        int result = 0;

        // getting increment by 1 only when the current window is possible to get manipulated
        int rightPointer = 0;

        // getting increment by 1 only when the current window is impossible to get manipulated
        int leftPointer = 0;

        while (rightPointer < s.length()) {
            freq[s.charAt(rightPointer) - 'A'] += 1;

            // tracks the highest frequency of any single character in the current sliding window
            maxFreq = Math.max(maxFreq, freq[s.charAt(rightPointer) - 'A']);
            windowSize = rightPointer - leftPointer + 1;

            // shrink the size of the window from the left until the number of replacements needed is <= k
            while (windowSize - maxFreq > k) {
                freq[s.charAt(leftPointer) - 'A'] -= 1;
                leftPointer++;
                windowSize = rightPointer - leftPointer + 1;
            }

            result = Math.max(result, windowSize);
            rightPointer++;
        }

        return result;
    }
}