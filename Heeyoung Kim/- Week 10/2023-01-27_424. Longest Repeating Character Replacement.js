// You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
// Return the length of the longest substring containing the same letter you can get after performing the above operations.

// Example 1:
// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.
// Example 2:

// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
// The substring "BBBB" has the longest repeating letters, which is 4.

var characterReplacement = function(s, k) {
    let left = 0, right = 0, maxchar=0;
    let map = {};
    
    while(right < s.length) {
        const char = s[right];
        map[char] = map[char] ? map[char]+1 : 1;
        
        if(map[char] > maxchar) maxchar = map[char];
        
        if(right-left+1-maxchar > k) {
            map[s[left]]--;
            left++;
        }

        right++;
    }
    
    return right-left;
};

//Time Complexity : O(n) => 연산이 수행 되는 횟수는 right++하면서 한번만 돌기 때문
//Space Complexity : O(1) ? O(n) => map 때문에 space 값을 가져가나..