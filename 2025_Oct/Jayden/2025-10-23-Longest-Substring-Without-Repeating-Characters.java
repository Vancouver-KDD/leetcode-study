class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(n)
    */
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<Character>();

        int leftPointer = 0;
        int rightPointer = 0;
        int longest = 0;

        while (rightPointer < s.length()) {
            char ch = s.charAt(rightPointer);

            // remove characters in set untill leftPointer reaches to closest ch from itself
            while (set.contains(ch)) {
                set.remove(s.charAt(leftPointer));
                leftPointer++;
            }

            set.add(ch);
            rightPointer++;
            longest = Math.max(longest, set.size());
        }

        return longest;

    }
}

/**
 * Given a string s, find the length of the longest substring without duplicate characters.
 *
 * ex)
 *
 * Input: s = "abcabcbb"
 * Output: 3
 *
 * - "abc"
 * - "bca"
 * - "cab"
 */