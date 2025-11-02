/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let left = 0,
    maxCount = 0;
  const freq = {};

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    freq[char] = (freq[char] || 0) + 1;
    maxCount = Math.max(maxCount, freq[char]);

    if (right - left + 1 - maxCount > k) {
      freq[s[left]]--;
      left++;
    }
  }

  return s.length - left;
};
