/**
 * Given two strings s and t of lengths m and n respectively, return the minimum window substring
 * of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
 * The testcases will be generated such that the answer is unique. 
 */

// 
public String minWindow(String s, String t) {
    if (s == null || t == null || s.length() < t.length()) {
        return "";
    }

    // Create a map to store the character count of t
    Map<Character, Integer> charCount = new HashMap<>();
    for (char c : t.toCharArray()) {
        charCount.put(c, charCount.getOrDefault(c, 0) + 1);
    }

    // Initialize the count of characters in t that need to be matched
    int count = charCount.size();

    // Initialize the left and right pointers for the sliding window
    int left = 0, right = 0;
    // Initialize the minimum window substring and its length
    String minWindow = "";
    int minLength = Integer.MAX_VALUE;

    while (right < s.length()) {
        // Move the right pointer and update the count of characters in the window
        char c = s.charAt(right);
        if (charCount.containsKey(c)) {
            charCount.put(c, charCount.get(c) - 1);
            if (charCount.get(c) == 0) {
                count--;
            }
        }
        right++;

        // If all characters in t have been matched, move the left pointer
        while (count == 0) {
            // Update the minimum window substring and its length
            if (right - left < minLength) {
                minWindow = s.substring(left, right);
                minLength = right - left;
            }

            // Move the left pointer and update the count of characters in the window
            c = s.charAt(left);
            if (charCount.containsKey(c)) {
                charCount.put(c, charCount.get(c) + 1);
                if (charCount.get(c) > 0) {
                    count++;
                }
            }
            left++;
        }
    }

    return minWindow;
}