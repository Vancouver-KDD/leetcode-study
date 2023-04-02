// Given a string s, find the length of the longest 
// substring without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

var legnthOfLongestSubstring = function(s) {
    let map = {};
    let windowStart = 0;
    let maxlength = 0;

    for(let i =0; i<s.length; i++) {
        let char = s[i];

        if(map[char] >= windowstart) windowstart  = map[char] + 1;
        map[char] = i;

        maxlength = Math.max(maxlength, i-windowstart+1);
    }

    return maxlength;
}

//Time complexity : O(n);
