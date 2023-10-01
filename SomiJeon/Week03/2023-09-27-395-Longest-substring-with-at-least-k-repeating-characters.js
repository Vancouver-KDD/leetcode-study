// Given a string s and an integer k,
//todo: return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

// if no such substring exists, return 0.

//* Example 1:

// Input: s = "aaabb", k = 3
// Output: 3
// Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

//* Example 2:

// Input: s = "ababbc", k = 2
// Output: 5
// Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
  if (s.length < k) {
    return 0;
  }

  if (k <= 1) {
    return s.length;
  }

  const charCount = new Map();
  for (let letter of s) {
    if (!charCount.has(letter)) {
      charCount.set(letter, 1);
    } else {
      charCount.set(letter, charCount.get(letter) + 1);
    }
  }

  // Check if every character in the string appears at least k times.
  let isEveryCharValid = true;
  for (let [char, count] of charCount) {
    if (count < k) {
      isEveryCharValid = false;
      break;
    }
  }

  if (isEveryCharValid) {
    return s.length; // If all characters meet the k requirement, the whole string is a valid substring.
  }

  let maxSubstringLength = 0;
  let start = 0;
  let end = 0;

  while (end < s.length) {
    if (charCount.get(s[end]) < k) {
      // When we find a character that appears less than k times, we split the string at that point.
      // The substring before the character is a potential valid substring.
      // We recursively call the function on the substring before the character.
      maxSubstringLength = Math.max(maxSubstringLength, longestSubstring(s.slice(start, end), k));
      start = end + 1;
    }
    end++;
  }

  // Handle the case where the last part of the string is a valid substring.
  maxSubstringLength = Math.max(maxSubstringLength, longestSubstring(s.slice(start), k));

  return maxSubstringLength;
};
