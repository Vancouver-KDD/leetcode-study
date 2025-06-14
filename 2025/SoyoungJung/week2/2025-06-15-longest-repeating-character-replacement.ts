function characterReplacement(s: string, k: number): number {
  const freq: number[] = new Array(26).fill(0);
  let left = 0;
  let maxCount = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    const idx = s.charCodeAt(right) - 65;
    freq[idx]++;
    maxCount = Math.max(maxCount, freq[idx]);

    const currentWindowSize = right - left + 1;

    if (currentWindowSize - maxCount > k) {
      const leftIdx = s.charCodeAt(left) - 65;
      freq[leftIdx]--;
      left++;
    }

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
