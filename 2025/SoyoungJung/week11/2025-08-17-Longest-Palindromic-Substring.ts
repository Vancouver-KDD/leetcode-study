function longestPalindrome(s: string): string {
  if (s.length < 2) return s;

  let start = 0;
  let maxLen = 1;

  const expandFromCenter = (left: number, right: number): void => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (right - left + 1 > maxLen) {
        maxLen = right - left + 1;
        start = left;
      }
      left--;
      right++;
    }
  };

  for (let i = 0; i < s.length; i++) {
    expandFromCenter(i, i);
    expandFromCenter(i, i + 1);
  }

  return s.substring(start, start + maxLen);
}
