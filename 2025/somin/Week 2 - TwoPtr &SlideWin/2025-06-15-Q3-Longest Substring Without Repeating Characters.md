```
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0, right = 0, maxLen = 0; // Pointers and max length
        HashSet<Character> longestSet = new HashSet<>(); // Stores unique characters in current window
        
        while (right < s.length()) {
            char r = s.charAt(right); // Current character to process

            // If character already exists in the set, move the left pointer
            // and remove characters until the duplicate is removed
            while (longestSet.contains(r)) {
                longestSet.remove(s.charAt(left));
                left++;
            }

            // Add the current character after removing duplicates
            longestSet.add(r);

            // Update max length if current window is longer
            maxLen = Math.max(maxLen, right - left + 1);

            // Move the right pointer to expand the window
            right++;
        }

        return maxLen;
    }
}

```

1. Time Complexity: O(n)
The right pointer traverses the string from left to right once → O(n)

The left pointer also moves at most n times across the entire string

Every character is added to and removed from the set at most once

So, even though it looks like a nested loop, it behaves like a sliding window, meaning:

Each character is processed at most twice (once in, once out)

👉 Total Time Complexity = O(n), where n = s.length().

2. Space Complexity: O(k) -> O(1)
- HashSet<Character> stores at most k unique characters at any time
- In the worst case (no duplicates), the set could grow up to the size of the string
