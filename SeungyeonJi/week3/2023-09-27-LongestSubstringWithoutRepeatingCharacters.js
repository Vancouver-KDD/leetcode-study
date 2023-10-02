var longestSubstring = function (s, k) {
  let uniqueLetterMax = new Set(s).size;
  let max = 0;

  for (let i = 1; i <= uniqueLetterMax; i++) {
    let right = 0;
    let left = 0;
    let map = new Map();
    let currUnique = 0;
    let kCount = 0;
    while (right < s.length) {
      map.set(s[right], (map.get(s[right]) || 0) + 1);

      if (map.get(s[right]) === 1) currUnique++;

      if (map.get(s[right]) === k) kCount++;

      while (currUnique > i) {
        if (map.get(s[left]) === k) kCount--;

        map.set(s[left], map.get(s[left]) - 1);

        if (map.get(s[left]) === 0) currUnique--;

        left++;
      }

      if (currUnique === kCount) max = Math.max(max, right - left + 1);

      right++;
    }
  }

  return max;
};
