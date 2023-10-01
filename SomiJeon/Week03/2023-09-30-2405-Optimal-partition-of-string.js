// Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

//todo: Return the minimum number of substrings in such a partition.

//! Note that each character should belong to exactly one substring in a partition.

//* Example 1:

// Input: s = "abacaba"
// Output: 4
// Explanation:
// "ab","a","cab","a" // is a valid partitioning as none of the characters appear more than once in the substring.
// It can be shown that 4 is the minimum number of substrings needed.

//* Example 2:

// Input: s = "ssssss"
// Output: 6
// Explanation:
// The only valid partition is ("s","s","s","s","s","s").

/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function (s) {
  if (s.length < 2) return s.length;

  const arrOfStr = s.split("");
  const set = new Set(arrOfStr);
  if (set.size === 1) return s.length;

  const uniqueChar = new Set();
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (!uniqueChar.has(s[i])) {
      uniqueChar.add(s[i]);
    } else {
      count++;
      uniqueChar.clear();
      uniqueChar.add(s[i]);
    }
  }
  return count + 1;
};
