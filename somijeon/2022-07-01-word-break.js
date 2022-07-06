// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

//* Example 1:

// Input: s = "applepenapple", wordDict = ["apple","pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
// Note that you are allowed to reuse a dictionary word.

//* Example 2:

// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
// Output: false

var wordBreak = function (s, wordDict) {
  const words = new Set(wordDict);
  const wordLens = new Set(wordDict.map((word) => word.length));
  const starts = new Set([0]);
  for (let start of starts) {
    for (let len of wordLens) {
      if (words.has(s.slice(start, start + len))) {
        starts.add(start + len);
      }
    }
  }
  return starts.has(s.length);
};
