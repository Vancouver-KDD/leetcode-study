function lengthOfLongestSubstring(s: string): number {
  if (s.length < 1) return 0;
  if (s.length === 1) return 1;

  let max = 1;
  for (let i = 0; i < s.length; i++) {
    const lookup = {};
    lookup[s[i]] = 1;

    let counting = 1;
    for (let j = i + 1; j < s.length; j++) {
      if (!lookup[s[j]]) {
        lookup[s[j]] = 1;
        counting++;
        max = Math.max(max, counting);
      } else {
        max = Math.max(max, counting);
        break;
      }
    }
  }

  return max;
}
